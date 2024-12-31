from flask import Flask
import math

app=Flask(__name__)

posts = {
    1:'post1',
    2:'post2',
    3:'post3',
    }

@app.route('/')
def index():
    return '<p>top page</p>'

@app.route('/hello')
def hello():
    return '<h1>こんにちは</h1>'

@app.route('/hello/<string:name1>/<string:name2>')
def show_name(name1, name2):
    return f'<h1>こんにちは{name1}さん{name2}さん</h1>'

@app.route('/add/<int:num1>/<int:num2>')
def add_num(num1, num2):
    return f'<h1>{num1 + num2}</h1>'

@app.route('/div/<float:num1>/<float:num2>')
def div_num(num1, num2):
    result=math.floor(num1/num2)
    return f'<h1>{result}</h1>'

@app.route('/post/<int:post_id>')
def get_posts(post_id):
    post=posts.get(post_id)
    return f'{post}'

@app.route('/user/<int:user_id>/<string:user_name>')
def show_user(user_id, user_name):
    return f'私はユーザー番号{user_id}の{user_name}です'

if __name__ == '__main__':
    app.run(debug=True)