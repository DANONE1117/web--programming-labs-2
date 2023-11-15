from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect('/menu', code=302)
@app.route('/lab1')
def lab1():     
    return '''
    <!doctype html>
     <link rel="stylesheet" href="''' + url_for('static', filename='main.css') + '''">
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
                    
                    <li> <a class='menu' href='/lab1/oak'> Дуб </a> </li>
                    <li> <a class='menu' href='/lab1/student'> студент </a> </li>
                    <li><a class='menu' href='/lab1/python'> пайтон </a> </li>
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
    <link rel="stylesheet" href="''' + url_for('static', filename='main.css') + '''">
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
                <li><a class='menu' href='/lab1'>Первая лабораторная</a></li>
                <li><a class='menu' href='/lab2/'>Вторая лабораторная</a></li>
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
    <link rel="stylesheet" href="''' + url_for('static', filename='main.css') + '''">
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
    <link rel="stylesheet" href="''' + url_for('static', filename='main.css') + '''">
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
    <link rel="stylesheet" href="''' + url_for('static', filename='main.css') + '''">
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
    fruits = [
        {'name' : 'Яблоки', 'price' : 100},
        {'name' : 'Груши', 'price' : 120},
        {'name' : 'Апельсины', 'price' : 80},
        {'name' : 'Мандарины', 'price' : 95}, 
        {'name' : 'Манго', 'price' : 321},
    ]
    books = [
        {'author' : 'Федор Достоевский', 'name' : 'Дурак', 'ganre' : 'Роман','page' : 523},
        {'author' : 'Джоан Роулин', 'name' : 'Десять негритят', 'ganre' : 'детектив','page' : 256},
        {'author' : 'Лев Толстой', 'name' : 'Война и мир', 'ganre' : 'фэнтези','page' : 320},
        {'author' : 'Агата Кристи', 'name' : 'Десять негритят', 'ganre' : 'классика','page' : 1274}, 
        {'author' : 'Федор Достоевский ', 'name' : 'Преступление и наказание', 'ganre' : 'классика','page' : 576},
        {'author' : 'Рэй Брэдбери', 'name' : '451 градус по Фаренгейту', 'ganre' : 'фантастика','page' : 256},
        {'author' : 'Джордж Оруэлл', 'name' : '1984', 'ganre' : 'фантастика','page' : 352},
        {'author' : 'Михаил Булгаков', 'name' : 'Мастер и Маргарита', 'ganre' : 'классика','page' : 480},
        {'author' : 'Эрнест Хемингуэй', 'name' : 'Старик и море', 'ganre' : 'классика','page' : 128},
        {'author' : 'Джек Лондон', 'name' : 'Белый клык', 'ganre' : 'приключения','page' : 256},  
          
    ]
    return render_template('example.html', name=name, number=number, group=group, Kurs=Kurs, fruits=fruits, books=books)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')
@app.route('/lab2/flowers')
def flowers():
    return render_template('flowers.html')