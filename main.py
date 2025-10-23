from typing import Final
import requests
import os


API_KEY: Final[str] = os.environ["CUTTLY_API_KEY"]
BASE_URL: Final[str] = 'https://cutt.ly/api/api.ph'


def shorten_link(full_link: str):
    payload: dict = {'key': API_KEY, 'short': full_link}
    request = requests.get(BASE_URL, params=payload)
    data: dict = request.json()


    if url_data:= data.get('url'):