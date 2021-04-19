from flask import render_template
from modules import callCrypt

def doCallUserRegForm(app, request, con):
  if request.method == "GET":
    return render_template('userRegForm.html', \
                            title = 'ユーザー登録画面(GET)', \
                            message = 'ユーザー名、パスワードを入力して下さい。')
  else:
    userName = request.form['userName']
    password = request.form['password']

    cursor = con.cursor()
    cursor.execute("INSERT INTO USERDATA VALUES('" + userName + "','"  + callCrypt.doCrypt(app, password) + "','"  + password + "', NOW())")
    con.commit()
    cursor.close()
    return render_template('userRegForm.html', \
                           title = 'ユーザー登録画面(POST)', \
                           message = '登録を完了しました。')

