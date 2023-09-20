from flask import Flask
app = Flask(__name__)

@app.route("/")
def start():
    return """
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
    """