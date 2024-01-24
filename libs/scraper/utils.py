# try to convert values to float format
def convert_data(data):
    data = data.strip()
    try:
        data_float = data.replace(".", "").replace(",", ".")

        # convert 10,5% to 10.5% value
        if data_float.endswith("%"):
            data_float = data_float[:-1]
            return f"{float(data_float)}%"

        # convert string value into float value
        return float(data_float)
    except ValueError:
        return data
