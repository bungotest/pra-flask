from flask import Flask, render_template, redirect

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/features')
def features():
    return render_template('features.html')


if __name__ == '__main__':
    app.run(debug=True)