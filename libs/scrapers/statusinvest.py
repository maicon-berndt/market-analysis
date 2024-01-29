import json
import pandas
import requests

from lxml import html

from libs.scrapers import (
    scraper,
    utils,
)

# Constants
REQUEST_HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "none",
    "accept-language": "en-US,en;q=0.9",
}


class StockListScraper(scraper.Scraper):
    def get_parsed_data(self) -> dict:
        # read csv file provided by Status Invest website with
        # the list of the stocks and their general information
        csv_df = pandas.read_csv(
            "https://statusinvest.com.br/category/AdvancedSearchResultExport?CategoryType=1&search=%7B%7D",
            sep=";",
            thousands=".",
            decimal=",",
            storage_options=REQUEST_HEADERS,
        )

        # applying strip to the column names (some of them have white spaces :S)
        csv_df.columns = [str(col_name).strip() for col_name in csv_df.columns]

        # set Ticker as index
        csv_df.set_index("TICKER", drop=False, inplace=True)
        csv_df.index.name = None

        return csv_df.T.to_dict()


class StockExtraInfosScraper(scraper.Scraper):
    def __init__(self, stock_ticker: str):
        self.ticket = stock_ticker

    def get_parsed_data(self) -> dict:
        # read list of stock details from fundamentus website
        html_data = requests.get(
            f"https://statusinvest.com.br/acoes/{self.ticket}",
            headers=REQUEST_HEADERS,
        )

        # parse HTML data
        tree = html.fromstring(html_data.text)

        # get historical vol info
        [vol_elem] = tree.xpath("//div[@data-volatility]")
        vol = utils.convert_data(vol_elem.attrib["data-ativo-volatility"])

        # get tag_along info
        [tag_along_elem] = tree.xpath("//span[text()='Tag Along']/../../div/strong")
        tag_along = utils.convert_data(tag_along_elem.text_content())

        # get options info
        [options_elem] = tree.xpath("//strong[text()='OPÇÕES']/../../div/strong")
        options = utils.convert_data(options_elem.text_content())

        # get corporate segment info
        [segment_elem] = tree.xpath("//h3[text()='Segmento de listagem']/../strong")
        segment = utils.convert_data(segment_elem.text_content())

        # get free float info
        [free_float_elem] = tree.xpath("//h3[text()='Free Float']/../../../strong")
        free_float = utils.convert_data(free_float_elem.text_content())

        return {
            "Vol Histórica": vol,
            "Tag Along": tag_along,
            "Tickers Opções": options,
            "Segmento": segment,
            "Free Float": free_float,
        }


class StockHistIndicatorsScraper(scraper.Scraper):
    def __init__(self, stock_ticker: str):
        self.ticket = stock_ticker

    def get_parsed_data(self) -> dict:
        # read list of stock details from fundamentus website
        json_str = requests.get(
            f"https://statusinvest.com.br/acao/indicatorhistoricallist?codes={self.ticket}&time=5",
            headers=REQUEST_HEADERS,
        )

        # parse json data
        json_data = json.loads(json_str.text)

        # return historical values for each indicator
        return {
            data["key"]: {
                rank_data["rank"]: rank_data["value"]
                for rank_data in data["ranks"]
                if "rank" in rank_data and "value" in rank_data
            }
            for data in list(json_data["data"].values())[0]
        }
