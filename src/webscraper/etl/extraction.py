import functools
import json
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.error import URLError
from urllib.parse import urljoin
from urllib.request import urlopen, Request

from bs4 import BeautifulSoup
from loguru import logger
from webscraper.utils.params import DATA_PATH


def open_page(url: str) -> str | None:
    logger.debug(f"Opening page: {url}...")
    req = Request(url)
    req.add_header("User-Agent", "Mozilla/5.0")
    try:
        return urlopen(req).read()
    except URLError as ex:
        logger.error(f"Could not open page: {url}. Error - {ex}")
        return None


def parse_core(html_page: str, class_obj: str) -> list[str]:
    soup = BeautifulSoup(html_page, "html.parser")
    allclass_div = soup.find("div", {"class": class_obj})

    if allclass_div:
        return [item.text.strip() for item in allclass_div.find("ul").find_all("li")]
    else:
        return []


def parse_part_numbers(html_page: str) -> list[str]:
    parts = parse_core(html_page, "allparts")
    return [element.split(" - ")[0] for element in parts]


def parse_categories(html_page: str) -> list[str]:
    cats = parse_core(html_page, "allcategories")
    return [element.replace(" ", "%20") for element in cats]


def parse_models(html_page: str) -> list[str]:
    models = parse_core(html_page, "allmodels")
    return [element.replace(" ", "%20") for element in models]


def parse_manufacturers(html_page: str) -> list[str]:
    manufacturers = parse_core(html_page, "allmakes")
    return [element.replace(" ", "%20") for element in manufacturers]


def get_man_cat_mdl_urls(url: str, n_pages: int | None) -> list[str]:
    html_page = open_page(url)
    if not html_page:
        return []
    manufacturers = parse_manufacturers(html_page)[:n_pages]
    man_url_list = [urljoin(f"{url}/", manufacturer) for manufacturer in manufacturers]
    man_cat_mdl_url_list = []
    # iterate over all manufacturers and create a list of pages to scrape
    for man_url in man_url_list:
        html_page = open_page(man_url)
        if not html_page:
            continue
        categories = parse_categories(html_page)
        # iterate over all categories and create a list of pages to scrape
        man_cat_url_list = [urljoin(f"{man_url}/", category) for category in categories]

        for man_cat_url in man_cat_url_list:
            html_page = open_page(man_cat_url)
            if not html_page:
                continue
            models = parse_models(html_page)
            # iterate over all models and create a list of pages to scrape
            man_cat_mdl_url_list.extend(
                [urljoin(f"{man_cat_url}/", model) for model in models]
            )

    return man_cat_mdl_url_list


def extract_part_numbers(
    url: str, persist: bool = False
) -> dict[str, list[str]] | None:
    html_page = open_page(url)
    if not html_page:
        res = {url: []}  # type: ignore
    else:
        res = {url: parse_part_numbers(html_page)}  # type: ignore

    if persist:
        scraped_data_path = DATA_PATH / "scraped"
        scraped_data_path.mkdir(exist_ok=True)
        with open(scraped_data_path / f"{uuid.uuid4().hex}.json", "w") as f:
            json.dump([res], f)
        return None
    else:
        return res


def scrape(
    url: str, n_pages: int | None = None, persist: bool = False
) -> list[dict[str, list[str]] | None]:
    logger.info(f"Scraping data from: {url}")

    logger.info("Extracting manufacturers, categories and models ...")
    url_list = get_man_cat_mdl_urls(url, n_pages)

    logger.info("Extracting part numbers ...")
    res = []
    with ThreadPoolExecutor() as executor:
        jobs = (
            executor.submit(
                functools.partial(extract_part_numbers, persist=persist), url
            )
            for url in url_list
        )
        for ftr in as_completed(jobs):
            res.append(ftr.result())

    return res
