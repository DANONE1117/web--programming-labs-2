from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect('/menu', code=302)
    '''
    <!doctype html>
    <html>
        <head>
            <title>Ковылин Даниил Артурович, Лабораторная работа 1</title>
        </head>
        <body>
            <header>
                НГТУ, ФБ, Лабораторная работа 1
            </header>

            <h1>web-сервер на flask</h1>

            <footer>
                &copy; Ковылин Даниил Артурович, ФБИ14, 3 курс, 2023
            </footer>
        </body>
    </html>
    '''
@app.route('/lab1')
def lab1():     
    return '''
    <!doctype html>
     <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <html>
        <head>
            <title>Ковылин Даниил Артурович, лабораторная 1</title>
        </head>
        <body>
            <header>
                НГТУ, ФБ, Лабораторная работа 1
            </header>
            <main>
                <h1>Web-сервер на flask</h1>

                <div>
                    Flask — фреймворк для создания веб-приложений на языке
                    программирования Python, использующий набор инструментов
                    Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
                    называемых микрофреймворков — минималистичных каркасов
                    веб-приложений, сознательно предоставляющих лишь самые ба-
                    зовые возможности.
                </div>
                <a href='/menu'> Меню</a>

                <h2>Реализованные роуты</h2>
                <ul>
                    
                    <li> <a href='/lab1/oak'> Дуб </a> </li>
                    <li> <a href='/lab1/student'> студент </a> </li>
                    <li><a href='/lab1/python'> пайтон </a> </li>
                </ul>



            </main>
            <footer>
                &copy; Ковылин Даниил Артурович, ФБИ-14, 3 курс, 2023
            </footer>
        </body>
    </html>
    '''
@app.route('/menu')
def menu():

    return '''
    <!doctype html>
     <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <html>
        <head>
            <title>НГТУ, ФБ, Лабораторные работы</title>
        </head>
        <body>
            <header>
                НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
            </header>
            <main>
                <ul>
                <li><a href='/lab1'>Первая лабораторная</a></li>
                <li><a href='/lab2/example'>Вторая лабораторная</a></li>
            </main>
            <footer>
                Ковылин Даниил Артурович, ФБИ-14, 3 курс, 2023
            </footer>
        </body>
    </html>
    '''

@app.route('/lab1/oak')
def oak():
    return '''
    <!doctype html>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <html> 
        <body>
            <header>
                НГТУ, ФБ, WEB-программирование, часть 2. 1 лабораторная
            </header>
    
            <h1>Дуб</h1>
            <img src="'''+ url_for('static', filename='dub.jpg') +'''">
        </body>
            <footer>
                Ковылин Даниил Артурович, ФБИ-14, 3 курс, 2023
            </footer>

    </html>
    '''

@app.route('/lab1/student')
def student():
    return '''
    <!doctype html>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <html>
        <body>
             <header>
                НГТУ, ФБ, WEB-программирование, часть 2. 1 лабораторная
            </header>

            <main>
                <h1 class='student'>Ковылин Даниил Артурович</h1>
                <img class='logo' src="'''+ url_for('static', filename='NSTULOG.png') +'''">
            </main>
            <footer>
                Ковылин Даниил Артурович, ФБИ-14, 3 курс, 2023
            </footer>
        </body>
    </html>
'''

@app.route('/lab1/python')
def python():
    return '''
    <!doctype html>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <html>
        <body>
            <header>
                НГТУ, ФБ, WEB-программирование, часть 2. 1 лабораторная
            </header>
    
            <main>
                <div>
                    <p>&nbsp;Python не требует явного объявления переменных, является регистро-зависим 
                    (переменная var не эквивалентна переменной Var или VAR — это три разные переменные) 
                    объектно-ориентированным языком.</p>
                    <p>Python содержит такие структуры данных как списки (lists), кортежи (tuples) и словари
                    (dictionaries). Списки — похожи на одномерные массивы 
                    (но вы можете использовать Список включающий списки — многомерный массив), 
                    кортежи — неизменяемые списки, словари — тоже списки, но индексы могут быть любого типа, 
                    а не только числовыми. "Массивы" в Python могут содержать данные любого типа, 
                    то есть в одном массиве может могут находиться числовые, строковые и другие типы данных. 
                    Массивы начинаются с индекса 0, а последний элемент можно получить по индексу -1 
                    Вы можете присваивать переменным функции и использовать их соответственно.</p>
                </div>
                <img class='python' src="'''+ url_for('static', filename='Python.png') +'''">
            </main>
            <footer>
                Ковылин Даниил Артурович, ФБИ-14, 3 курс, 2023
            </footer>
        </body>
    </html>
'''
@app.route('/lab2/example')
def example():
    name = 'Ковылин Даниил'
    number = 'лабораторная работа 2'
    group = 'ФБИ-14'
    Kurs = '3 курс'
    return render_template('example.html', name=name, number=number, group=group, Kurs=Kurs)