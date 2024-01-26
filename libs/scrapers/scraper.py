import pandas


class Scraper:
    _data_dict = None

    def get_parsed_data(self) -> dict:
        raise NotImplementedError(
            f"{self.__class__.__name__}.get_parsed_data is not implemented"
        )

    def run(self) -> None:
        self._data_dict = self.get_parsed_data()

    @property
    def dict_format(self) -> dict:
        if not self._data_dict:
            self.run()
        return self._data_dict

    @property
    def dataframe_format(self) -> pandas.DataFrame:
        dd = self.dict_format
        return pandas.DataFrame.from_dict(dd, orient="index")

    def to_excel(self, file_path) -> None:
        df = self.dataframe_format

        xlsx = pandas.ExcelWriter(file_path)
        df.to_excel(xlsx, index=False)

        # convert percentage values
        sheet = xlsx.book.worksheets[0]

        rows_count = len(df)
        for idx, column in enumerate(df.columns):
            if (
                hasattr(df[column], "str")
                and len(df[df[column].str.endswith("%")]) == rows_count
            ):
                for row_idx in range(2, sheet.max_row):  # ignore header row
                    cell = sheet[row_idx][idx]
                    cell.number_format = "0.00%"
                    cell.value = float(cell.value.rstrip("%")) / 100

        # save and close
        xlsx.close()
