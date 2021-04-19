import bcrypt

def doCrypt(app,password):
   return bcrypt.hashpw(password.encode(), app.config["CRYPTKEY"]).decode()

def doCheckPassword(password, hashedPassword):
  return bcrypt.checkpw(password.encode(), hashedPassword.encode())
