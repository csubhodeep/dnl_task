from webscraper.etl.extraction import scrape
from webscraper.etl.loading import load
from webscraper.etl.transformation import transform
from webscraper.utils.params import BASE_URL


def run_pipeline():
    """This is the main pipeline that orchestrates the ETL process.
    This version would only work if all the scraped data can fit into the memory at once.
    :return:
    """
    data = scrape(BASE_URL)
    df = transform(data)
    load(df)


# An experimental version of the pipeline that could potentially be used for larger (OOM) datasets.
# def run_parallelized_pipeline():
#     """This version of the pipeline only makes sense when a limited amount of data can fit into the memory.
#     Primarily, this does the following:
#     1. Scrapes the data parallely and saves it to disk.
#     2. Loads a limited number of chunks from the disk, transforms them and loads it to the database parallely.
#     :return:
#     """
#     def _transform_load(file: pathlib.Path) -> None:
#         with open(file, "r") as f:
#             data = json.load(f)
#         df = transform(data)
#         load(df)
#
#     scrape(BASE_URL, persist=True, n_pages=2)
#
#     files = DATA_PATH.joinpath("scraped").glob("*.json")
#     res = []
#     with ThreadPoolExecutor() as executor:
#         jobs = (executor.submit(_transform_load, file) for file in files)
#
#         for ftr in as_completed(jobs):
#             res.append(ftr.result())


if __name__ == "__main__":
    run_pipeline()
