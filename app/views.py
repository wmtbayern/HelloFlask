from flask import Blueprint, request, make_response, url_for, redirect, abort, render_template, session

blue=Blueprint('simple_page',__name__)
#simple_page   相当于django里面的  namespace

#可以多个路由指向一个视图函数
@blue.route('/')

@blue.route('/index/')

def index():
    # return 'hello_world'
    # name=session.get('name','游客')

    name=request.cookies.get('name')
    content='这个是传递过来的参数'

    #render_template  可以将参数返回,里面也是字符串
    return render_template('index.html',content={
        'name':name
    })
#flask 的路由规则:   必须以 //  开始结尾

#带参数的路由写法:  <参数名称> 值直接写在url 里面

@blue.route('/setname/<string:name>/')

def setname(name):
    return 'hello:'+name
@blue.route('/setage/<int:age>/')
def setage(age):
    return  '年龄:'+ str(age)
@blue.route('/setscore/<float:score>/')
def setscore(score):
    return  '你的成绩是:' + str(score)
@blue.route('/getop/<any(a,b,c):op>/')
def getop(op):
    return '套餐类型:'+ op

@blue.route('/getaaa1/<any(a,v,s,w):op>/')
def rrrr(op):
    return "您的套餐:"+op
@blue.route('/getpath/<path:where>/')
def getpath(where):
    return '我的位置:'+ where

# 我的位置:sfsf/sfs/12343

#where 后面的都是  path参数  的 内容
#声明请求方法的在  methods 里面写明 以列表的形式
@blue.route('/requesttest/',methods=['get','put','post'])
def re():
    data={
        '请求方法:':request.method,
        '请求路径':request.path,
        '请求url':request.url,
        'get请求参数':request.args,
        'post请求参数':request.form,
        '请求的文件':request.files,
        'cookie':request.cookies
    }
    return str(data)
# TypeError: 'dict' object is not callable
# The view function did not return a valid response.
# The return type must be a string, tuple, Response instance,
# or WSGI callable, but it was a dict.

#response 相应
@blue.route('/response/',methods=['get','post'])
def response():
    #反向解析  url_for()   '蓝图名字.视图名字'
    url_path=url_for('simple_page.index')

    response=redirect(url_path)

    return response

    #return redirect(url_path) 两者是一样的结果,url_for 和 redirect一起使用,完成重定向
#抛出异常
@blue.route('/errtest/')
def erro():
    abort(404)   #抛出异常
#捕获异常
#当出现abort(参数)
#跳转到   errorhandler  的路由

#然后进入这个视图函数进行处理

#注意前后的状态码要一致

@blue.errorhandler(404)   #处理异常
#视图函数叫什么名字无所谓,参数一致就可以了
def err404(e):
    #返回给客户端的是字符串,可以带标签
    return '<h1>我不是404</h1>'
@blue.route('/login/',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    elif request.method=='POST':

        name=request.form.get('name')

        response=redirect(url_for('simple_page.index'))

        #状态保持,要先设置session密钥
        # session['name']=name


        response.set_cookie('name',name,max_age=60*60*1)
        return response
@blue.route('/register/', methods=['GET','POST'])
def register():

    if request.method=="GET":
        return render_template('register.html')
        # return 'heksks'
    elif request.method=="POST":
        name=request.form.get('name')
        # url_for('蓝图名.函数名'),反向解析的写法
        response = redirect(url_for('simple_page.index'))
        #设置cookie
        response.set_cookie('name', name, max_age=60 * 60 * 2)
        # kk=request.cookies.get()
        #获取cookie request.cookies.get('')
        #删除cookie
        # response.delete_cookie(key)
        # 返回首页
        return response
@blue.route('/logout/')
def logout():

    response=redirect(url_for('simple_page.index'))

    response.delete_cookie('name')  #默认是存储在内存当中,没有做持久化存储

    # response.delete_cookie('session')
    # session.pop('name')   删除
    return response

