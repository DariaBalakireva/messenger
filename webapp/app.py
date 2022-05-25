import time

import flask
from flask import Flask, abort

app = Flask(__name__)
db = []
for i in range(3):
    db.append({
        'name': 'Anton',
        'time': time.time(),
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
    # TODO
    # проверить, является ли присланное пользователем правильным json-объектом
    # проверить, есть ли там имя и текст
    # Добавить сообщение в базу данных db
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
    message = {
        'text': text,
        'name': name,
        'time': time.time()
    }
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
    users = set()
    messages_quantity = 0
    for j in db:
            messages_quantity += 1
            users.add('<li>' + j['name'] + '</li>')

    return "<p><strong>STATUS:</strong></p>" \
            "<p>Quantity of users: {users_quantity}</p>" \
            "<p>List of users: <ul>{users}</ul></p>" \
            "<p>Quantity of messages: {messages_quantity}</p>".format(
        users_quantity = len(users),
        users =''.join(users),
        messages_quantity = messages_quantity
            )

if __name__ == '__main__':
    app.run(host='0.0.0.0')