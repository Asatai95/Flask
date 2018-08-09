from flask import Flask, request, render_template, redirect, make_response, url_for

application = Flask(__name__)

@application.route('/')
def test():

    return render_template('index.html')

@application.route('/test')
def db():

    return "やっとできたー"

@application.route('/app')
def test_sub():

    return "なんだかな"

if __name__ == '__main__':
    app.run()
