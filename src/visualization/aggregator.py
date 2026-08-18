import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "storage"))

from db import get_all_news
from collections import Counter
from datetime import datetime


def get_daily_news_count() -> dict:
    """
    DB에 저장된 뉴스를 날짜별로 집계하는 함수.
    반환 예: {"2026-06-15": 3, "2026-06-16": 5}
    """
    news_list = get_all_news()

    date_counter = Counter()
    for news in news_list:
        pub_date = news["pub_date"]
        # pubDate 형식 예: "Mon, 15 Jun 2026 09:00:00 +0900"
        parsed_date = datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S %z")
        date_str = parsed_date.strftime("%Y-%m-%d")
        date_counter[date_str] += 1

    return dict(sorted(date_counter.items()))

if __name__ == "__main__":
    result = get_daily_news_count()
    print(result)