from flask import Flask, redirect
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
                НГТУ, ФБ, Лабораторная работ 1
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
    <html>
        <head>
            <title>НГТУ, ФБ, Лабораторные работы</title>
        </head>
        <body>
            <header>
                НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
            </header>
            <main>
                <a href='/lab1'>Первая лабораторная</a>
            </main>
            <footer>
                Ковылин Даниил Артурович, ФБИ-14, 3 курс, 2023
            </footer>
        </body>
    </html>
    '''