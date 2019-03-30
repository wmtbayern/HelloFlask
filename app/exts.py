
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy


#第三方插件的初始化都在这里,

#db的实例化
db=SQLAlchemy()
sess=Session()
migrate=Migrate()
def init_ext(app):
    #初始化第三方插件,就是让实例化出来的对象调用  init_app() 方法,传入参数 app
    db.init_app(app)
    sess.init_app(app)
    migrate.init_app(app,db)
