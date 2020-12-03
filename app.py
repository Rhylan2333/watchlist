# 修改视图函数返回值
from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index') # 修改 URL 规则，之绑定多个URL
@app.route('/home') # 修改 URL 规则，之绑定多个URL
def hello():
    return '<h1>Hello CaiCai!</h1><img src="http://helloflask.com/totoro.gif">' # 这是一个网址中的内容


# 修改 URL 规则，之使用escape()
from flask import escape

@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % escape(name)


# 修改视图函数名
from flask import url_for

@app.route('/test')
def test_url_for():
    # 下面是一些调用示例（请在cmd查看输出的 URL）：
    print(url_for('hello'))  # 输出：/
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('user_page', name='greyli'))  # 输出：/user/greyli
    print(url_for('user_page', name='CaiCai'))  # 输出：/user/CaiCai
    print(url_for('test_url_for'))  # 输出：/test
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
    print(url_for('test_url_for', num=2))  # 输出：/test?num=2
    return 'Test page'
