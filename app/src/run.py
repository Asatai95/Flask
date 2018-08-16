import pymysql
import os
from flask import Flask, request, render_template, redirect, make_response, url_for
from werkzeug import secure_filename
from werkzeug.exceptions import BadRequest

application = Flask(__name__)

UPLOAD_FOLDER = './static/img/'
ALLOWED_EXTENSIONS = set(['png', 'jpeg', 'gif'])
path = './static/img/*.ALLOWED_EXTENSIONS'
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):

    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@application.route('/')
def hougen():

    return render_template('docker.html')

@application.route('/', methods=['POST'])
def top_db():

    search = request.form['search']

    db = pymysql.connect(host='172.19.0.1', user='root', password='asatai951156', db='docker', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    con = db.cursor()
    print('???')

    sql = 'select h_y, miyako from hougen where miyako = "'+ search +'" '
    text = con.execute(sql)
    db.commit()
    print(sql)
    print(text)

    if text == 0:

        print('test')

        return render_template('search.html', test=search)

    result = con.fetchall()
    print(result)

    return render_template('search.html', text=result)

@application.route('/info')
def info():

    return render_template('info.html')

@application.route('/images')
def image():

    db = pymysql.connect(host='172.19.0.1', user='root', password='asatai951156', db='docker', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    con = db.cursor()
    print('???')

    sql = 'select id ,img, post, comment from img'
    test = con.execute(sql)
    db.commit()
    print(sql)
    print(test)

    result = con.fetchall()
    print(result)

    return render_template('image.html', test=result)

@application.route('/images/<img_test>')
def img_db(img_test=None):

    db = pymysql.connect(host='172.19.0.1', user='root', password='asatai951156', db='docker', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    con = db.cursor()
    print('???')

    sql = 'select id, img, post, comment from img where id = "' + img_test + '" '
    img_db = con.execute(sql)
    db.commit()
    print(sql)
    print(img_db)

    result = con.fetchall()
    print(result)

    return render_template('images.html', imgs=result)

@application.route('/images/image_post')
def image_test():

    return render_template('image_post.html')

@application.route('/images/image_post', methods=['POST'])
def remake():

    user = request.form['user']
    user_comment = request.form['comment']
    img_file = request.files['img_file']
    print(img_file)
    print(user)
    print(user_comment)

    try:

        if user == (''):

            test = 'ユーザー名を入力してください。'

            return render_template('image_post.html', error=test)

        elif user_comment == (''):

            test = 'None'

            if img_file and allowed_file(img_file.filename):

                filename = secure_filename(img_file.filename)
                img_file.save(os.path.join(application.config['UPLOAD_FOLDER'], filename))
                path = UPLOAD_FOLDER + filename
                print(path)

                db = pymysql.connect(host='172.19.0.1', user='root', password='asatai951156', db='docker', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
                con = db.cursor()
                print('???')

                sql = 'insert into img(img, post, comment) values(%s, %s, %s)'
                try:
                    test = con.execute(sql, [path, user, test])
                    db.commit()
                    print(sql)
                    print(test)

                    result = con.fetchall()
                    print(result)

                    return redirect('http://localhost:8080/images')

                except BadRequest:

                    test = '画像選択してください。'

                    return render_template('image_post.html', error=test)
            else:
                path = './static/img/yuryou.png'
                test = '画像を選択してください。'

                db = pymysql.connect(host='172.19.0.1', user='root', password='asatai951156', db='docker', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
                con = db.cursor()
                print('???')

                sql = 'insert into img(img) values(%s)'
                test = con.execute(sql, [path])
                db.commit()
                print(sql)
                print(test)

                result = con.fetchall()
                print(result)

                return render_template('image_post.html', error=test)

        elif user == ('') and user_comment == (''):

            test = '全ての項目を入力してください。'

            return render_template('image_post.html', error=test)

        else:

            try:

                if img_file and allowed_file(img_file.filename):

                    filename = secure_filename(img_file.filename)
                    img_file.save(os.path.join(application.config['UPLOAD_FOLDER'], filename))
                    path = UPLOAD_FOLDER + filename
                    print(path)

                    db = pymysql.connect(host='172.19.0.1', user='root', password='asatai951156', db='docker', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
                    con = db.cursor()
                    print('???')

                    sql = 'insert into img(img, post, comment) values(%s, %s, %s)'
                    test = con.execute(sql, [path, user, user_comment])
                    db.commit()
                    print(sql)
                    print(test)

                    result = con.fetchall()
                    print(result)

                    return redirect('http://localhost:8080/images')

                else:

                   path = './static/img/yuryou.png'
                   test = '画像を選択してください。'

                   db = pymysql.connect(host='172.19.0.1', user='root', password='asatai951156', db='docker', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
                   con = db.cursor()
                   print('???')

                   sql = 'insert into img(img) values(%s)'
                   test = con.execute(sql, [path])
                   db.commit()
                   print(sql)
                   print(test)

                   result = con.fetchall()
                   print(result)

                   return render_template('image_post.html', error=test)

            except werkzeug.exceptions.BadRequest:

               path = '../static/img/error.jpeg'

               return render_template('image_post.html', error=path)

    except werkzeug.exceptions.BadRequest:

        path = '../static/img/error.jpeg'

        return render_template('image_post.html', error=path)


if __name__ == '__main__':
    app.run()
