#coding:utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis

app = Flask(__name__)


class Config(object):

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/ihome_project'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

app.config.from_object(Config)
#创建数据库连接
db = SQLAlchemy(app)

redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)


@app.route('/index')
def index():
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)