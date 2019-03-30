from flask_migrate import Migrate
from flask_bootstrap import Bootstrap




from manage import app



#bootstrap 初始化
Bootstrap(app)
#迁移文件初始化
migrate=Migrate()

def init_ext(app):
    migrate.init_app(app,db)

#flask_migrate 命令相关

# python manage.py db init  生成对应的文件目录,(只需要调用一次)
# python manage.py db migrate  生成对应的迁移文件
# python manage.py db migrate   --mesage  'xxx'   生成对应的迁移文件(标注信息)
# python manage.py db upgrade  创建表的过程
# python manage.py db downgrade  删除表的过程
