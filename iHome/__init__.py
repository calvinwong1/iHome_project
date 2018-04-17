#coding:utf-8

from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
import redis
# from config import Config, Development, Production, UnitTest
from config import configs

# 创建数据库连接对象
db = SQLAlchemy()

def get_app(configs_name):
    app = Flask(__name__)

    #加载配置参数
    app.config.from_object(configs[configs_name])

    #创建数据库连接对象
    # db = SQLAlchemy(app)
    db.init_app(app)

    #开启CSRF
    csrf = CSRFProtect(app)

    #创建连接到redis数据库的对象
    redis_store = redis.StrictRedis(host=configs[configs_name].REDIS_HOST, port=configs[configs_name].REDIS_PORT)

    #使用flask_session扩展将session存放到redis数据库中
    Session(app)

    return app