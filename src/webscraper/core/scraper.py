from __future__ import annotations

import requests
from bs4 import BeautifulSoup
from webscraper.utils import params


def scrape():
    response = requests.get(params.BASE_URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    return None
