import os
import requests
from dotenv import load_dotenv

load_dotenv()

NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")


def fetch_naver_news(query: str, display: int = 100) -> dict:
    """
    네이버 뉴스 검색 API를 실제로 호출하는 함수.
    """
    url = "https://naverapihub.apigw.ntruss.com/search/v1/news"
    headers = {
        "X-NCP-APIGW-API-KEY-ID": NAVER_CLIENT_ID,
        "X-NCP-APIGW-API-KEY": NAVER_CLIENT_SECRET,
    }
    params = {
        "query": query,
        "display": display,
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()