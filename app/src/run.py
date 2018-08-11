import pymysql
from flask import Flask, request, render_template, redirect, make_response, url_for

application = Flask(__name__)

@application.route('/')
def test():

    test = 'test'

    db = pymysql.connect(host='172.19.0.1', user='root', password='asatai951156', db='docker', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    con = db.cursor()
    print('???')

    sql = 'select id, test from test where id = 2'
    con.execute(sql)
    db.commit()
    print('test')

    result = con.fetchall()
    print(result)

    return render_template('index.html', data=result)

@application.route('/', methods=['POST'])
def top_test():

    test_text = request.form['test']
    print(test_text)

    db = pymysql.connect(host='172.19.0.1', user='root', password='asatai951156', db='docker', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    con = db.cursor()
    print('???')

    sql = 'insert into test(test) values(%s) '
    con.execute(sql, [test_text])
    db.commit()

    result_test = con.fetchall()
    print(result_test)

    return render_template('index.html')

@application.route('/test')
def db():

    test = 'docker'

    resp = make_response(render_template('test.html', test_sub='testだよ'))
    test_resp = resp.set_cookie("name" ,test)
    print(resp)
    print(test_resp)

    return resp

@application.route('/app')
def test_sub():

    return "なんだかな"

if __name__ == '__main__':
    app.run()
