import requests


class DataHandler:
    # https://console.cloud.google.com/marketplace/browse?filter=solution-type:dataset&filter=price:free&q=med
    # https://clinicaltrials.gov/data-api/api
    # https://beta-ut.clinicaltrials.gov/api/oas/v2.html
    API_ENDPOINT_URI = "some uri"

    def __init__(self) -> None:
        pass

    def fetch_data(self):
        result = requests.request("get", "https://www.google.com/")
        if result.status_code == 200:
            return result
        return None
