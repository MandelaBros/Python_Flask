from flask import render_template
from modules import callCrypt

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
    chkFlg = callCrypt.doCheckPassword(password, data[0])
    cursor.close()
    if chkFlg:
            return render_template('loginForm.html', \
                           title = 'ログイン画面(POST)', \
                           message = '認証情報を確認しました。')
    else:
            return render_template('loginForm.html', \
                           title = 'ログイン画面(POST)', \
                           message = '認証情報を確認できませんでした。')
