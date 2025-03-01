import io
import base64
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 한글 폰트 경로 설정
FONT_PATH = "./static/fonts/NotoSansKR-Regular.ttf"


def generate_wordcloud(text):
    """입력된 텍스트로 워드 클라우드를 생성하고 Base64 인코딩된 이미지 데이터를 반환"""
    wordcloud = WordCloud(font_path=FONT_PATH, width=800, height=400, background_color="white")
    wordcloud.generate(text)

    # 이미지 데이터를 메모리에 저장
    img_io = io.BytesIO()
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(img_io, format="png", bbox_inches="tight")
    plt.close()

    img_io.seek(0)
    img_base64 = base64.b64encode(img_io.read()).decode("utf-8")

    return img_base64
