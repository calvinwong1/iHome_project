#coding:utf-8

from flask import Flask,session
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
# from iHome import app, db
from iHome import get_app, db

app = get_app('dev')

#Flask_script集成
manager = Manager(app)

#数据库迁移集成, 让迁移时，app和db建立关联
Migrate(app, db)
# 将数据库迁移的脚本、命令添加到脚本管理器对象
manager.add_command('db', MigrateCommand)


@app.route('/index', methods=['GET', 'POST'])
def index():
    # 设置session
    # session['name'] = 'ojl'

    return 'index'


if __name__ == '__main__':
    #使用脚本管理器运行程序
    manager.run()