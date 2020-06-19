import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'abcdef1234567890!@#$%^000!!!'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db') + '?check_same_thread=False'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
