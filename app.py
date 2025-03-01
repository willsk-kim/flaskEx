from flask import Flask, render_template, request
from wordCloud import generate_wordcloud  # 분리된 파일에서 함수 가져오기

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    wordcloud_img = None

    if request.method == "POST":
        text = request.form["text"]  # 입력된 텍스트 가져오기
        wordcloud_img = generate_wordcloud(text)  # 워드 클라우드 생성

    return render_template("wordCloud.html", wordcloud_img=wordcloud_img)

if __name__ == "__main__":
    app.run()
