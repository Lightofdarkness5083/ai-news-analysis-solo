import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__)))

import matplotlib.pyplot as plt
from aggregator import get_daily_news_count

import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False


def draw_daily_trend_chart(save_path: str = "output/daily_trend.png"):
    """
    일자별 뉴스 건수를 라인차트로 그려서 이미지 파일로 저장하는 함수.
    """
    daily_counts = get_daily_news_count()

    dates = list(daily_counts.keys())
    counts = list(daily_counts.values())

    plt.figure(figsize=(10, 5))
    plt.plot(dates, counts, marker="o")
    plt.title("일자별 뉴스 건수 추이")
    plt.xlabel("날짜")
    plt.ylabel("건수")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(save_path)
    print(f"[차트] {save_path} 에 저장 완료")

if __name__ == "__main__":
        draw_daily_trend_chart()
