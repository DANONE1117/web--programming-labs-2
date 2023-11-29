from flask import Blueprint, render_template, request
lab4 = Blueprint('lab4', __name__)

@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')


@lab4.route('/lab4/login', methods= ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'Даниил' and password == '0000':
        return render_template('success1.html', username = username)
    elif username == '' or password == '':
        error1 = 'Заполните поля!'
        return render_template('login.html', error1=error1, username = username, password = password)
    else:
        error2 = 'Неверные логин и/или пароль'
        return render_template('login.html', username = username, error2=error2, password = password)


