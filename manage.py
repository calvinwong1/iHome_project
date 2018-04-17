#coding:utf-8

from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
import redis
from flask_script import Manager

from flask_migrate import Migrate,MigrateCommand



class Config(object):
    '''配置参数'''

    #设置调试模式
    DEBUG = True

    #秘钥
    SECRET_KEY = 'ihome'

    #配置mysql数据库：真实开发中不会使用127,，会根据真实数据库地址与端口进行指向
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/ihome_project'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #配置redis数据库：实际开发使用redis数据库的真实ip
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    #配置session参数
    #指定session储存的redis
    SESSION_TYPE = 'redis'
    #是否使用secret_key签名session_data
    SESSION_USE_SIGNER = True
    #指定要使用的redis的位置
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    #设置session的过期时间
    PERMANENT_SESSION_LIFETIME = 3600 * 24 #过期时间为一天


app = Flask(__name__)

#加载配置参数
app.config.from_object(Config)

#创建数据库连接
db = SQLAlchemy(app)

#开启CSRF
csrf = CSRFProtect(app)

#创建连接到redis数据库的对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

#使用flask_session扩展将session存放到redis数据库中
Session(app)

#Flask_script集成
manager = Manager(app)

#数据库迁移集成, 让迁移时，app和db建立关联
Migrate(app, db)
# 将数据库迁移的脚本、命令添加到脚本管理器对象
manager.add_command('db', MigrateCommand)


@app.route('/index')
def index():
    # 设置session
    session['name'] = 'ojl'

    return 'index'


if __name__ == '__main__':
    #使用脚本管理器运行程序
    manager.run()