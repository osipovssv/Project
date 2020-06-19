from app import db
from app.models import User, Post


users_data =[
    {'email': 'example1@mail.ru', 'password': '123456'},
    {'email': 'example2@mail.ru', 'password': '12345678'},
    {'email': 'example3@mail.ru', 'password': 'qwerty6'},
    {'email': 'example1@gmail.com', 'password': 'QWERTY'},
    {'email': 'example1@yandex.ru', 'password': '123456'},
    {'email': 'aaaaaaaaa@mail.ru', 'password': '000'},
]

for data in users_data:
    u = User(email=data['email'], password=data['password'])
    db.session.add(u)

db.session.commit()
