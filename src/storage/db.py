import sqlite3
import os


DB_PATH = "output/data/news.db"


def init_db():
    """
    SQLite DB에 연결하고, news 테이블이 없으면 새로 만드는 함수.
    """
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            link TEXT NOT NULL UNIQUE,
            pub_date TEXT
        )
    """)

    conn.commit()
    conn.close()
    print(f"[DB] {DB_PATH} 에 news 테이블 준비 완료")

def save_news(news_list: list[dict]):
    """
    뉴스 리스트를 DB에 저장하는 함수.
    link가 이미 있으면(중복이면) 건너뛴다.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    saved_count = 0
    skipped_count = 0

    for news in news_list:
        try:
            cursor.execute("""
                INSERT INTO news (title, link, pub_date)
                VALUES (?, ?, ?)
            """, (news["title"], news["link"], news["pub_date"]))
            saved_count += 1
        except sqlite3.IntegrityError:
            # link가 UNIQUE 제약을 위반한 경우 (이미 존재하는 URL)
            skipped_count += 1

    conn.commit()
    conn.close()
    print(f"[DB] 저장 {saved_count}건, 중복 스킵 {skipped_count}건")  

def get_all_news() -> list[dict]:
    """
    DB에 저장된 모든 뉴스를 조회하는 함수.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT id, title, link, pub_date FROM news")
    rows = cursor.fetchall()

    conn.close()

    result = []
    for row in rows:
        result.append({
            "id": row[0],
            "title": row[1],
            "link": row[2],
            "pub_date": row[3],
        })
    return result

if __name__ == "__main__":
    init_db()

    test_news = [
        {"title": "코스피 2900 돌파", "link": "https://n.news.naver.com/article/101", "pub_date": "Mon, 15 Jun 2026 09:00:00 +0900"},
        {"title": "코스닥 강세 지속", "link": "https://n.news.naver.com/article/102", "pub_date": "Mon, 15 Jun 2026 10:00:00 +0900"},
    ]
    save_news(test_news)

    # 같은 데이터를 한 번 더 저장 시도 (중복 체크 테스트)
    save_news(test_news) 

    print(get_all_news()) 