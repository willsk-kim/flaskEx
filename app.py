import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from flask import Flask, render_template, request, send_file
import io
import base64

app = Flask(__name__)

# 1. 워드 클라우드 생성 함수
def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color="white")
    wordcloud.generate(text)

    # 2. 이미지 데이터를 메모리에 저장
    img_io = io.BytesIO()
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(img_io, format="png", bbox_inches="tight")
    plt.close()
    img_io.seek(0)

    # 3. 이미지 데이터를 Base64로 인코딩하여 HTML에서 표시 가능하도록 변환
    img_base64 = base64.b64encode(img_io.read()).decode("utf-8")

    return img_base64

# 4. 홈 페이지 - 텍스트 입력 폼 및 워드 클라우드 표시
@app.route("/", methods=["GET", "POST"])
def index():
    wordcloud_img = None

    if request.method == "POST":
        text = request.form["text"]  # 입력된 텍스트 가져오기
        wordcloud_img = generate_wordcloud(text)  # 워드 클라우드 생성

    return render_template("index.html", wordcloud_img=wordcloud_img)

# 5. 서버 실행
if __name__ == "__main__":
    app.run(debug=True)
