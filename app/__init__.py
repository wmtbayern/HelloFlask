from flask import Flask
#from flask.ext.session import Session  老版本的倒包
from flask_session import Session

from app.exts import init_ext
from app.settings import init_app
from app.views import blue, init_view
from app.models import  db

#感觉__init__文件就是Django 里面的settings文件,数据库配置, static的配置
# ,蓝图的配置   flask 的初始化都是在这里完成

#flask官网有个extents的,有各种扩展插件的内容
# 看官方文档,安装插件,配置插件,使用插件
# blueprint,用于路由规划

def create_app(env_name='default'):
    #app是flask的实例
    #初始化flask
    app = Flask(__name__)

    init_app(app,env_name)

    init_view(app)

    init_ext(app)
    # #配置session  ,
    # app.config['SECRET_KEY']='@#danvdjw23()##@@@45kjnf#@$$#@mnj1243535'
    # #\
    # app.config['SESSION_TYPE']='redis'
    # #初始化   方式一
    # Session(app)
 # _------------------------------
    #初始化,方式二
    # sess=Session()  #先实例化
    # sess.init_app(app)  #调用初始化方法
    #蓝图的注册
    # app.register_blueprint(blueprint=blue)
    # app.register_blueprint(blue)  注册的第二种写法
    #配置sqlite的方法
    # ///   相对路径
    # ////  绝对路径
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite3.db'

    #配置mysql的方法
                                            #数据库名+对应的驱动 用户  密码     主机     端口  数据库名字
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/HelloFlask'
    # #禁止对象追踪修改
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    # #初始化,
    # db.init_app(app)

    return app
# 需求: 项目拆分(MTV)

#拆分flask 项目的时候 ,各个文件之间关系混乱

#解决办法是  引入blueprint

#蓝图插件 blueprint 主要用来规划路由

#实例化,初始化配置
#simple_page 是反向解析用到的,类似django的命名空间
# blue=Blueprint('simple_page',__name__)
