# 主页
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '我是主页'


if __name__ == "__main__":
    app.run(debug=True,port=8000)

