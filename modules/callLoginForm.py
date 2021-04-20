from flask import render_template
from modules import callCrypt, callSesshion

def doCallLoginForm(app, request, con):
  if request.method == "GET":
    return render_template('loginForm.html', \
                            title = 'ログイン画面(GET)', \
                            message = 'ユーザー名、パスワードを入力して下さい。')
  else:
    userName = request.form['userName']
    password = request.form['password']
    cursor = con.cursor()
    cursor.execute("SELECT PASSWORD FROM USERDATA WHERE NAME = '" + userName + "'")
    data = cursor.fetchone()
    if data is None:
      return render_template('loginForm.html', \
                           title = 'ログイン画面(POST)', \
                           message = '認証情報を確認できませんでした。')

    chkFlg = callCrypt.doCheckPassword(password, data[0])
    cursor.close()
    if chkFlg:
            callSesshion.doSetSession()
            return render_template('menuForm.html', \
                           title = 'メニュー画面')
    else:
            return render_template('loginForm.html', \
                           title = 'ログイン画面(POST)', \
                           message = '認証情報を確認できませんでした。')
