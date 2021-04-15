from flask import Flask
from flask import render_template
from modules import callAozoraList
 
app = Flask(__name__)
 
@app.route('/')
def index():
    values = {"val1": 100, "val2" :200}
    return render_template('index.html', values=values)

@app.route('/aozoraList')
def aozoraList():
    list = callAozoraList.doCallAozoraList()
    return render_template('aozoraList.html', list=list)

if __name__ == '__main__':
    app.run()