#coding:utf-8

from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
import redis
from config import Config, Development, Production, UnitTest

app = Flask(__name__)

#加载配置参数
app.config.from_object(Development)

#创建数据库连接
db = SQLAlchemy(app)

#开启CSRF
csrf = CSRFProtect(app)

#创建连接到redis数据库的对象
redis_store = redis.StrictRedis(host=Development.REDIS_HOST, port=Development.REDIS_PORT)

#使用flask_session扩展将session存放到redis数据库中
Session(app)