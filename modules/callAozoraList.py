from flask import render_template, Response
from modules import callSesshion

def doCallAozoraList(app, con):
  if callSesshion.doCheckSession() == False:
     return callSesshion.doLogout()

  cursor = con.cursor()
  cursor.execute("SELECT AUTHOR,BOOK FROM AOZORA")
  data = cursor.fetchall()
#  print(json.dumps(data, indent=2))
  retList = list()
  for dat in data:
    retList.append("著者名：" + dat[0] + "：作品名：" + dat[1])

  cursor.close()
  return render_template('aozoraList.html', list=retList)

#CSVダウンロード
def doCsvDownLoad(con):
  cursor = con.cursor()
  cursor.execute("SELECT AUTHOR,BOOK FROM AOZORA")
  data = cursor.fetchall()
  csvStr = ""
  for dat in data:
    csvStr += "著者名：" + dat[0] + "：作品名：" + dat[1] + "\n"
  cursor.close()

  return Response(
        csvStr,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=aozoraList.csv"})
