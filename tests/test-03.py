from app import db
from app.models import User, Post


user = User.query.filter(User.password == '12345').all()

print(user)

# SELECT *
# FROM tableName
# WHERE id=5
