import pandas

from libs.scrapers import (
    scraper,
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

        return csv_df.T.to_dict()
