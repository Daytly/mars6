from flask import Flask, url_for, request, render_template, redirect
import json
from auth import LoginForm

app = Flask(__name__)


@app.route('/index/<title>')
def index1(title):
    return render_template('base.html', title=title)


@app.route('/answer')
def training():
    _dict = {'Фамилия': ' Watny',
             'Имя': 'Mark',
             'Образование': 'выше среднего',
             'Профессия': 'штурман марсохода',
             'Пол': 'male',
             'Мотивация': 'Всегда мечтал застрять на Марсе!',
             'Готовы остаться на Марсе?': True}
    return render_template('answer.html', dict=_dict)


app.run(port=8080, host='127.0.0.1')
