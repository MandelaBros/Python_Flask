from flask import render_template

import json

def doCallAozoraList(app, con):
  cursor = con.cursor()
  cursor.execute("SELECT AUTHOR,BOOK FROM AOZORA")
  data = cursor.fetchall()
#  print(json.dumps(data, indent=2))
  retList = list()
  for dat in data:
    retList.append("著者名：" + dat[0] + "：作品名：" + dat[1])

  cursor.close()
  return render_template('aozoraList.html', list=retList)
