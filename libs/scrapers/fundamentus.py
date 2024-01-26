import requests

from lxml import html

from libs.scrapers import (
    scraper,
    utils,
)

# Constants
REQUEST_HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}


class StockListScraper(scraper.Scraper):
    def get_parsed_data(self) -> dict:
        # read list of stocks with general data from fundamentus website
        html_data = requests.get(
            "http://www.fundamentus.com.br/resultado.php",
            headers=REQUEST_HEADERS,
        )

        # parse HTML data
        tree = html.fromstring(html_data.text)

        # get main table data
        [table] = tree.xpath("//table[@id='resultado']")

        # get table head data
        [thead] = table.xpath("thead")
        [tr] = thead.xpath("tr")
        headers = [th.text_content().strip() for th in tr.xpath("th")]

        # get table body data
        [tbody] = table.xpath("tbody")

        # parse and return dict with all stocks general infos
        data = {}

        for tr in tbody.xpath("tr"):
            body_data = [
                utils.convert_data(i.text_content().strip()) for i in tr.xpath("td")
            ]
            stock_data = dict(zip(headers, body_data))
            tick = stock_data["Papel"]
            data[tick] = stock_data

        return data


class StockDetailsScraper(scraper.Scraper):
    def __init__(self, stock_ticker: str):
        self.ticket = stock_ticker

    def get_parsed_data(self) -> dict:
        # read list of stock details from fundamentus website
        html_data = requests.get(
            f"http://www.fundamentus.com.br/detalhes.php?papel={self.ticket}",
            headers=REQUEST_HEADERS,
        )

        # parse HTML data
        tree = html.fromstring(html_data.text)

        # get content tables
        tables = tree.xpath("//table")

        # parse tables content
        data = {}

        for table in tables:
            for tr in table.xpath("tr"):
                td_label = [
                    i.xpath("span")[-1].text_content().strip()
                    for i in tr.xpath("td")
                    if "label" in i.attrib.get("class")
                ]

                td_data = [
                    utils.convert_data(i.xpath("span")[-1].text_content().strip())
                    for i in tr.xpath("td")
                    if "data" in i.attrib.get("class")
                ]

                while td_label:
                    key = td_label.pop(0)
                    value = td_data.pop(0)

                    if key:
                        while key in data:
                            key += "_"
                        data[key] = value

        return data
