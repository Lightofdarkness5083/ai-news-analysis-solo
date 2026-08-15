# naver_news_collector.py

MOCK_RESPONSE = {
    "items": [
        {
            "title": "삼성전자, AI 반도체 신제품 공개",
            "originallink": "https://example.com/news1",
            "link": "https://n.news.naver.com/article/001",
            "pubDate": "Mon, 15 Jun 2026 09:00:00 +0900"
        },
        {
            "title": "네이버, 클로바 AI 업데이트 발표",
            "originallink": "https://example.com/news2",
            "link": "https://n.news.naver.com/article/002",
            "pubDate": "Mon, 15 Jun 2026 10:30:00 +0900"
        },
        {
            "title": "카카오, 신규 AI 서비스 출시 예고",
            "originallink": "https://example.com/news3",
            "link": "https://n.news.naver.com/article/003",
            "pubDate": "Tue, 16 Jun 2026 08:15:00 +0900"
        }
    ]
}
def fetch_naver_news(query: str, display: int = 100) -> dict:
    """
    네이버 뉴스 검색 API를 호출하는 함수.
    지금은 목 데이터를 리턴하지만, 나중에 API 키가 준비되면
    이 함수 내부만 실제 requests.get() 호출로 바꾸면 된다.
    """
    print(f"[MOCK] '{query}' 검색어로 뉴스 {display}건 요청 (실제 API 대신 목 데이터 사용)")
    return MOCK_RESPONSE

if __name__ == "__main__":
    result = fetch_naver_news("AI 반도체")
    print(result)