import bcrypt

rounds=12
print(bcrypt.gensalt(rounds))

#def hash_password(password, rounds=12):
#    return bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds)).decode()

#def check_password(hashed_password, user_password):
#    return bcrypt.checkpw(user_password.encode(), hashed_password.encode())
