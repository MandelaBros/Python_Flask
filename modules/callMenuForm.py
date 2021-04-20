from flask import render_template
from modules import callCrypt, callSesshion

def doCallLoginForm():
  if callSesshion.doCheckSession() == false:
     return callSesshion.doLogout()

  return render_template('menuForm.html')
