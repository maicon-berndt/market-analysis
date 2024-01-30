import requests

from lxml import html

try:
    from libs.scrapers import (
        scraper,
    )
except:
    import scraper

# Constants
REQUEST_HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
}


class StockInfosScraper(scraper.Scraper):
    def __init__(self, stock_ticker: str):
        self.ticker = stock_ticker

    def get_parsed_data(self) -> dict:
        html_data = requests.get(
            f"https://fundamentei.com/br/{self.ticker}",
            headers=REQUEST_HEADERS,
        )

        # parse HTML data
        tree = html.fromstring(html_data.text)

        # get companies name
        company_name = tree.xpath("//h1[contains(.,'•')]")[0].text

        # get users score info
        users_score = tree.xpath("//h3[contains(.,' / ')]")[0].text

        # get listing segment info
        b3_segment = tree.xpath("//h6[text()='Segmento de Listagem']/../span")[
            0
        ].text_content()

        # get tag along info
        tag_along_divs = tree.xpath("//h6[text()='Tag Along']/../div/div")
        tag_along = " - ".join([elem.text_content() for elem in tag_along_divs])

        # get free float info
        free_float_divs = tree.xpath("//h6[text()='Free Float']/../div/div")
        free_float = " - ".join([elem.text_content() for elem in free_float_divs])

        return {
            "Nome da Empresa": company_name,
            "Nota dos Usuários": users_score,
            "Segmento de Listagem": b3_segment,
            "Tag Along": tag_along,
            "Free Float": free_float,
        }
