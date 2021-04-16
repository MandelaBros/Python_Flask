from flask import render_template
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

def doCallUserRegForm(app, request, con):
  if request.method == "GET":
    return render_template('inputForm2.html', \
                            title = 'ユーザー登録画面(GET)', \
                            message = 'ユーザー名、パスワードを入力して下さい。')
  else:
    userName = request.form['userName']
    password = request.form['password']

    cursor = con.cursor()
    cursor.execute("INSERT INTO USERDATA VALUES('" + userName + "','"  + doEncryptPassword(password) + "', NOW())")
    cursor.close()
    return render_template('inputForm2.html', \
                           title = 'ユーザー登録画面(POST)', \
                           message = '登録を完了しました。')

def doEncryptPassword(password):
    # TODO password暗号化
    ePassword = password
    return ePassword
