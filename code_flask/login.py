# 主页
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '我是主页'

# 添加注册页面
@app.route('/login')
def login():
    return '我是注册页面'

if __name__ == "__main__":
    app.run(debug=True,port=8000)

