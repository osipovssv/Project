from app import db
from app.models import User, Post


# Получаем список всех пользователей
all_users = User.query.all()

for index, user in enumerate(all_users):
    print(f'{index + 1}. ID: {user.id} Email: {user.email}, Пароль: {user.password}')
