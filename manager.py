from flask.ext.wtf import CSRFProtect
from redis import StrictRedis
from flask import Flask, session
from flask.ext.sqlalchemy import SQLAlchemy
# 在终端输入: pip install flask-session,再去导入 Session
# 作用:可以用来指定 session 保存的位置
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import Config
from information.info import app ,db



# 6.设置成命令行执行代码的方式:manager
# 作用:可以添加 数据库迁移 的功能,因为要用到命令的方式
manager = Manager(app)
# # 7.数据库的迁移
Migrate(app, db)  # 将app 与 db 关联
manager.add_command('db', MigrateCommand)  # 将迁移命令添加到manager


@app.route("/")
def index():
    # session['name'] = 'elaiza'  # 测试redis数据
    return "index"


if __name__ == "__main__":
    # 如果想右键运行:可以将runserver添加到 manager.py的 Script parameters(在Edit Configurations里)
    manager.run()
