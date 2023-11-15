from flask import Flask, redirect, url_for, render_template
from lab1 import lab1
app = Flask(__name__)
app.register_blueprint(lab1)


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