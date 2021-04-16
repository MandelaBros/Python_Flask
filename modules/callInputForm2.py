from flask import render_template

def doCallInputForm2(app, request, con):
  if request.method == "GET":
    return render_template('inputForm2.html', \
                            title = '入力テスト画面２(GET)', \
                            message = '何かを入力して下さい。', \
                            list = doSelectInput(con))
  else:
    inputText = request.form['inputText']
    cursor = con.cursor()
    cursor.execute("INSERT INTO INPUTDATA VALUES('" + inputText + "', NOW())")
    cursor.close()
    return render_template('inputForm2.html', \
                           title = '入力テスト画面２(POST)', \
                           message = '入力されたものは{}です。'.format(inputText), \
                           list = doSelectInput(con))

def doSelectInput(con):
  cursor = con.cursor()
  cursor.execute("SELECT TEXT FROM INPUTDATA")
  data = cursor.fetchall()
  retList = list()
  for dat in data:
    retList.append(dat[0])

  cursor.close()
  return retList