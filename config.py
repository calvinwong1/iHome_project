#coding:utf-8

import redis


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

class Development(Config):
    '''开发模式下的配置'''
    pass

class Production(Config):
    '''上线模式配置'''
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/ihome'
    PERMANENT_SESSION_LIFETIME = 3600 * 24 *7  # 过期时间为一星期

class UnitTest(Config):
    '''测试模式下的配置'''
    #开启测试模式
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/ihome_unittest'