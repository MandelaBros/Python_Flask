import mysql.connector
import json

def doCallAozoraList():

  conn = mysql.connector.connect(
      host='localhost',
      port='3306',
      user='root',
      password='passwd',
      database='python'
  )
  cursor = conn.cursor()
  cursor.execute("SELECT AUTHOR,BOOK FROM AOZORA")
  data = cursor.fetchall()
  print(json.dumps(data, indent=2))

  retList = list()
  for dat in data:
    retList.append("著者名：" + dat[0] + "：作品名：" + dat[1])

  cursor.close()
  conn.close()
  return retList
