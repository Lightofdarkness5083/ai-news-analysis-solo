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
    url = "https://openapi.naver.com/v1/search/news.json"
    headers = {
        "X-Naver-Client-Id": NAVER_CLIENT_ID,
        "X-Naver-Client-Secret": NAVER_CLIENT_SECRET,
    }
    params = {
        "query": query,
        "display": display,
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()