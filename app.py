from flask import Flask, jsonify, render_template, request  # request 추가

app = Flask(__name__)

# 모든 이미지 리스트
all_outfits = [
    "outfit1.jpg", "outfit2.jpg", "outfit3.jpg", "outfit4.jpg", "outfit5.jpg",
    "outfit6.jpg", "outfit7.jpg", "outfit8.jpg", "outfit9.jpg", "outfit10.jpg",
    "outfit11.jpg", "outfit12.jpg", "outfit13.jpg", "outfit14.jpg", "outfit15.jpg"
]

# 한 번에 로드할 이미지 개수
IMAGES_PER_PAGE = 5

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/load-images')
def load_images():
    # 현재 페이지 번호 가져오기
    page = int(request.args.get('page', 1))  # request 사용
    start = (page - 1) * IMAGES_PER_PAGE
    end = start + IMAGES_PER_PAGE

    # 페이지 범위에 해당하는 이미지 전달
    images = all_outfits[start:end]
    return jsonify({'images': images})

if __name__ == '__main__':
    app.run(debug=True)

    app.run(debug=True)


