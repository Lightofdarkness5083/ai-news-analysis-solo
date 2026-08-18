import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def summarize_news(title: str, content: str = "") -> str:
    """
    뉴스 제목(및 내용)을 받아 OpenAI로 한 문장 요약을 만드는 함수.
    """
    prompt = f"다음 뉴스를 한국어로 한 문장으로 요약해줘.\n\n제목: {title}\n내용: {content}"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    summary = response.choices[0].message.content
    return summary

def analyze_insight(news_titles: list[str]) -> str:
    """
    여러 뉴스 제목을 받아 전체적인 트렌드나 시사점을 분석하는 함수.
    """
    titles_text = "\n".join(f"- {title}" for title in news_titles)
    prompt = f"""다음은 오늘 수집된 주식 시장 관련 뉴스 제목들이다.
이 뉴스들을 종합해서 전체적인 시장 흐름과 주요 시사점을 3줄 이내로 분석해줘.

{titles_text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    insight = response.choices[0].message.content
    return insight

if __name__ == "__main__":
    result = summarize_news(
        title="코스피 2900 돌파, 외국인 매수세 지속",
        content="코스피 지수가 개인과 외국인의 동반 매수에 힘입어 2900선을 돌파했다."
    )
    print("[요약]", result)

    insight = analyze_insight([
        "코스피 2900 돌파, 외국인 매수세 지속",
        "코스닥 강세, 이차전지 업종 급등",
        "반도체 수출 호조에 관련주 동반 상승",
    ])
    print("[인사이트]", insight)