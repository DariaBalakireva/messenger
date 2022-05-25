import requests
name = input('Введите имя: ')
while len(name) == 0:
    name = input('Имя должно быть заполнено.Пожалуйста введите имя: ')
anon = input('Если хотите отправлять сообщения анонимно, введите "да": ')
if anon == "да" or anon == "Да" or anon == "ДА" or anon == "yes" or anon == "Yes" or anon == "y":
    # поправка на глупость
    name = 'Аноним'



while True:
    text = input('Введите сообщение: ')
    response = requests.post('http://127.0.0.1:5000/send',
                             json={
                                 'name': name,
                                 'text': text
                             }
                            )