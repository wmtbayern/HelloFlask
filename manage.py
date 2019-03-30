from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager

#flask_script(第一个插件)

#用于接收命令行参数,支持两种参数

# runserver,
# shell脚本的自定义命令

#  manger=Manager(Flask对象)

from app import create_app

app = create_app()

#实例化Manager,参数是flask实例化出来的对象

manager=Manager(app)
migrate=Migrate(app)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    #manager 的使用
    manager.run()
# python manage.py runserver #基本操作,启动项目
# python manage.py runserver  --help #查看帮助,
# python manage.py runserver  -h  host  #主机名,
# python manage.py runserver  -p  port  #端口,
# python manage.py runserver  -d  debug  #开启调试模式
# python manage.py runserver  -r  reload  #自动重新加载,
# python manage.py runserver  -r  -d

#视图之request
#请求参数 包括 路径参数,  get参数   post参数
#格式  <参数类型:变量名>
# 例如:<string:name>
#    int/float/string/uuid/any/path/
#要注意的是    路径参数的名字应该和视图函数的参数名一致
# @blue.route('/getname/<string:name>/')
# def getname(name)  视图函数的参数名字必须是name


# flask 的反向解析   url_for('蓝图命.函数名')  (要解析到哪个函数名???)')
# 注意和重定向的区别   redirect('/index/')

# request对象
# 服务器收到客户端的请求后,会自动创建出request对象,不能修改[全局内置对象,所有的函数都有的]
# 可以由request对象拿到我们想要的信息//
#对于web应用,客户端发送给服务器的数据十分重要,
# 在flask中由 request对象 提供这些信息
# request.method  请求方法
# request.path   请求路径
# request.url    请求的url
# request.args  get请求的参数
# request.form  .post 请求的参数
# request.headers  请求头,
# request.cookies    获取cookies的内容,,,,,,,,,,
# request.args['name']  ,值如果不存在会报错,
# request.args.get('name')  不存在返回None 推荐使用,
# request.args.get('name','0')  可以设置默认值

#视图之response
#需要手动创建,然后return 返回给客户端
#直接返回字符串,    返回模板render_template [也是字符串]
#  make_response()    response对象
#  Response()         response对象 后面可以跟上状态码
#  2XX 成功  3XX 重定向  4XX 客户端错误  5XX服务端错误
#response=Response('响应',200)


#基于项目的可扩展性和代码的可阅读性,当代码量很大时,将所有的代码都写在一个文件是很糟糕的,
# 所以我们要对 flask 文件进行拆分,主要还是参考django 的 mtv 模式来进行,
# 将不同的功能放在其对应的模块中,方便阅读,
# 将主要的执行内容写在执行文件 manage.py 中,引入flask-script 插件管理app
#创建appa文件目录,将views和models写入其中进行管理

#当一个请求传入时,web服务器决定生成一个新的线程(或者别的什么东西
# ,只要这个底层的对象可以胜任并发系统,而不仅是线程),当flask 开始他的内部请求处理时,
# 它认定当前线程是活动的环境,并绑定当前的应用和WSGI环境到那个线程上
# ,能保证一个应用调用另一个应用时不会出错


