from flask import Flask, session, redirect, request, render_template

def doSetSession():
    session['loginFlg'] = True

def doRemoveSession():
    session['loginFlg'] = False

def doCheckSession():
    if session.get("loginFlg"):
        return True
    return False

def doLogout():
    return render_template('loginForm.html', \
                title = 'ログイン画面', \
                message = '認証情報を確認できませんでした。')

