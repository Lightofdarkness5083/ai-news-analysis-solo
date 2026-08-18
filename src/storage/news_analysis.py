import sqlite3

def init_analysis_table(db_path="output/data/news.db"):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS news_analysis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            period_start TEXT,
            period_end TEXT,
            category TEXT,
            trend_summary TEXT,
            keywords TEXT,
            key_issues TEXT,
            created_at TEXT
        )
    """)
    conn.commit()
    conn.close()
    print("[DB] news_analysis 테이블 생성 완료")

if __name__ == "__main__":
    init_analysis_table()