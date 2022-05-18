# save this as app.py
import time

import flask
from flask import Flask, abort

app = Flask(__name__)
db = []
for i in range(3):
    db.append({
        'name': 'Anton',
        'time': 12343,
        'text': 'text01923097'
    })

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/send", methods= ['POST'])
def send_message():
    '''
    функция для отправки нового сообщения пользователем
    :return:
    '''
    data = flask.request.json
    if not isinstance(data, dict):
        return abort(400)

    if 'name' not in data or \
        'text' not in data:
        return abort(400)

    if not isinstance(data['name'], str) or \
        not isinstance(data['text'], str) or \
        len(data['name']) == 0 or \
        len(data['text']) == 0:
        return abort(400)

    text = data['text']
    name = data['name']

    if text[0] == '*':
        name = 'Анонимус'

    message = {
        'text': text,
        'name': name,
        'time': time.time()
    }

    if text == '/help':
        message['text'] = 'Попробуйте команды: /clear, /me. Начните сообщение со звездочки (*), чтобы отправить его анонимно'
        db.append(message)
    elif text == '/clear':
        db.clear()
        message['text'] = 'История очищена'
        message['name'] = 'server'
        db.append(message)
    elif text == '/me':
        s = set()
        for i in db:
            nm = i['name']
            if nm == name:
                message['text'] = f'Вы {len(s)+1}-ый пользователь!'
                message['name'] = 'server'
                db.append(message)
                break
            if nm != 'server':
                s.add(nm)
    else:
        db.append(message)

    return {'ok': True}

@app.route("/messages")
def get_messages():
    try:
        after = float(flask.request.args['after'])
    except:
        abort(400)
    db_after = []
    for message in db:
        if message['time'] > after:
            db_after.append(message)
    return {'messages': db_after}

@app.route("/status")
def print_status():
    names = set()

    for i in db:
        names.add(i['name'])

    return f'<h1>В чате {len(names)} участников: {names} и {len(db)} сообщений</h1>'




app.run()