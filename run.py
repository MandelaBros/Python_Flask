from flask import Flask, render_template, request
from modules import callAozoraList, callInputForm1, callUserRegForm, callLoginForm
from datetime import timedelta
import mysql.connector
import logging

app = Flask(__name__)
#設定ファイル読み込み
app.config.from_pyfile('prop.ini')
#セッションキー
app.secret_key = app.config["SESSION_KEY"]
app.permanent_session_lifetime = timedelta(minutes=3)

#DB接続
con = mysql.connector.connect(
    host=app.config["HOST"],
    port=app.config["PORT"],
    user=app.config["USER"],
    password=app.config["PASSWORD"],
    database=app.config["DATABASE"]
)
#ログレベル設定
logging.basicConfig(level=logging.INFO)

#index 
@app.route('/')
def index():
    values = {"val1": 100, "val2" :200}
    return render_template('index.html', values=values)

#青空文庫一覧
@app.route('/aozoraList')
def aozoraList():
    return callAozoraList.doCallAozoraList(app, con)

#CSVダウンロード
@app.route('/aozoraList/csvDownLoad', methods=["GET", "POST"])
def csvDownLoad():
    return callAozoraList.doCsvDownLoad(con)

#入力テスト画面１
@app.route('/inputForm1', methods=["GET", "POST"])
def inputForm1():
    return callInputForm1.doCallInputForm1(app, request)

#ユーザー登録画面
@app.route('/userRegForm', methods=["GET", "POST"])
def userRegForm():
    return callUserRegForm.doCallUserRegForm(app, request, con)

#ログイン画面
@app.route('/loginForm', methods=["GET", "POST"])
def loginForm():
    app.logger.info('侵入者有')
    return callLoginForm.doCallLoginForm(app, request, con)

if __name__ == '__main__':
    app.run()