import requests


class GoogleDrive:
    url = "https://drive.google.com/uc?export=download&id="
    client = requests

    def __init__(self, url: str):
        self.source_url = url

    def get_source(self) -> str:
        url = self.source_url
        file_id = url.split('/')[-2]
        download_url = self.url + file_id

        response = self.client.get(download_url)

        if response.status_code != 200:
            raise Exception("Page not found")
        return response.text
