

#flask 没有提供任何的数据库操作API
#我们可以选择任何适合自己业务需求的数据库来使用,
#flask  可以使用原生的sql 也可以使用ORM  (SQLAlchemy  MongoEngine)  (插件思维)
# 原生的sql 使用起来代码复用性比较差,可阅读性差,,

#python 的 ORM  (SQLAlchemy)
from flask_sqlalchemy import SQLAlchemy

from app.exts import db


class Student(db.Model):
    #对表进行重新命名
    __tablename__='student'
    #记得对合适的字段进行主键的定义
    s_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    s_name=db.Column(db.String(20))
    s_age=db.Column(db.Integer)
    #创建表单
    db.create_all()

    #删除表单
    # db.drop_all()
    #插入数据
    # stu=Student()
    # stu.s_name='测试'
    # stu.s_age=19
    # db.session.add(stu)
    # db.session.commit()

#在flask 中,主键是需要自己定义的,否则会报错,(每个模型对应一个表单,每个表单都需要一个主键)!
