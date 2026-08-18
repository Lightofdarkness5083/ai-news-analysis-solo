import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "collector"))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "storage"))

from naver_news_collector import fetch_naver_news, parse_news_items, NAVER_CLIENT_ID, NAVER_CLIENT_SECRET
from db import init_db, save_news

print("ID:", repr(NAVER_CLIENT_ID), "len:", len(NAVER_CLIENT_ID))
print("SECRET:", repr(NAVER_CLIENT_SECRET), "len:", len(NAVER_CLIENT_SECRET))

if __name__ == "__main__":
    init_db()
    result = fetch_naver_news("주식 시장")
    parsed = parse_news_items(result)
    save_news(parsed)
    print(f"{len(parsed)}건 수집 및 저장 완료")