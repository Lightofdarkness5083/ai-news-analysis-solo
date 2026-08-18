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



def parse_news_items(api_response: dict) -> list[dict]:
    """
    API 응답(dict)에서 news 리스트를 뽑아
    DB 저장에 필요한 형태로 정리하는 함수.
    """
    items = api_response.get("items", [])
    parsed = []
    for item in items:
        parsed.append({
            "title": item["title"],
            "link": item["link"],
            "pub_date": item["pubDate"],
        })
    return parsed