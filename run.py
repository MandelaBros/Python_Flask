from flask import Flask, render_template, request
from modules import callAozoraList, callInputForm1, callInputForm2
import mysql.connector

app = Flask(__name__)
#設定ファイル読み込み
app.config.from_pyfile('prop.ini')
#DB接続
con = mysql.connector.connect(
    host=app.config["HOST"],
    port=app.config["PORT"],
    user=app.config["USER"],
    password=app.config["PASSWORD"],
    database=app.config["DATABASE"]
)

#index 
@app.route('/')
def index():
    values = {"val1": 100, "val2" :200}
    return render_template('index.html', values=values)

#青空文庫一覧
@app.route('/aozoraList')
def aozoraList():
    return callAozoraList.doCallAozoraList(app, con)

#入力テスト画面１
@app.route('/inputForm1', methods=["GET", "POST"])
def inputForm1():
    return callInputForm1.doCallInputForm1(app, request)

#入力テスト画面２
@app.route('/inputForm2', methods=["GET", "POST"])
def inputForm2():
    return callInputForm2.doCallInputForm2(app, request, con)

#ユーザー登録画面
@app.route('/userRegForm', methods=["GET", "POST"])
def userRegForm():
    return callUserRegForm.doCallUserRegForm(app, request)

if __name__ == '__main__':
    app.run()