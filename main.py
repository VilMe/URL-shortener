from typing import Final
import requests
import os


API_KEY: Final[str] = os.environ["CUTTLY_API_KEY"]
BASE_URL: Final[str] = 'https://cutt.ly/api/api.ph'

