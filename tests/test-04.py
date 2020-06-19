from app import db
from app.models import User, Post


users = User.query.filter(User.password == '123456').all()
for user in users:
    print(user)
