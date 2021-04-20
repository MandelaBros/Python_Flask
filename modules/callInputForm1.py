from flask import render_template
from modules import callCrypt, callSesshion

def doCallInputForm1(app, request):
  if callSesshion.doCheckSession() == False:
     return callSesshion.doLogout()

  if request.method == "GET":
    return render_template('inputForm1.html', \
                            title = '入力テスト画面１(GET)', \
                            message = '何かを入力して下さい。')
  else:
    inputText = request.form['inputText']
    return render_template('inputForm1.html', \
                           title = '入力テスト画面１(POST)', \
                           message = '入力されたものは{}です。'.format(inputText))
