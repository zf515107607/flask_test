# from flask import Flask, render_template, flash, redirect, url_for
# from flask_script import Manager,Server
# from user.forms import LoginForm
# from user import app
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
# @app.route('/index/')
# def index():
#     user='jack'
#     return render_template('index.html',user = user,title = 'zhufeng')
#
# @app.route('/login/',methods=['GET','POST'])
# def login():
#     form = LoginForm()
#     # 验证表格中的数据格式是否正确
#     if form.validate_on_submit():
#         # 闪现的信息会出现在页面，当然在页面上要设置
#         flash('用户登录的名户名是:{} , 是否记住我:{}'.format(
#             form.username.data, form.remember_me.data))
#         # 重定向至首页
#         return redirect(url_for('index'))
#     # 首次登录/数据格式错误都会是在登录界面
#     return render_template('login.html',title='登录',form = form)
from operator import and_, or_



from flask import Blueprint, render_template



from app.ext import db

from .models import User



"""



"""

user = Blueprint('user', __name__)





# 过滤函数

# 执行查询函数

# fLask 1.0

@user.route('/show/')

def show():

    # 过滤列

    query = db.session.query(User.name).all()

    # 查询所有的行跟列

    users = User.query.all()

    user = User.query.filter_by(name='test1').first()

    #     # 过滤行

    # filter 可以使用运算符

    users = User.query.filter(User.name == 'xm').all()

    #  select  uid,name from user  where nam='xm' and passwo=123456

    return '查询'





# 过滤器

@user.route('/1/')

def filter01():

    name = 'test'

    # %s%

    User.query.filter(User.name.like('%' + name + '%'))

    # s%

    User.query.filter(User.name.startswith())

    # %s

    User.query.filter(User.name.endswith())

    # IN  NOT IN

    User.query.filter(~User.name.in_(['t', 's', 'c']))

    # is null

    User.query.filter(User.name is None)

    # is not null

    User.query.filter(User.name is not None)

    User.query.filter(and_(User.name == 'test1', User.weight > 120.00))

    # 也可以

    # User.query.filter(User.name == 'test1').filter(User.weight > 120.00)

    # or

    User.query.filter(or_(User.name == '小明', User.desc.like('%说%')))

    return '常用的操作符'





"""

page*size

select  * from user

limit 0 10

"""





# page   pagezize

# 分页

# limit  表示去多少条数据

# offset 表示偏移量  表示从设置的偏移量大小+1开始获取数据

# 计算最大页数





#



@user.route('/limit/<int:page>/<int:size>/')

def query_limit(page, size):

    # 注意:做分页的不需要设置执行函数

    # users = db.session.query(User.name, User.uid, User.create_date).order_by(User.uid).limit(size).offset(

    #     (page - 1) * size)

    #

    # total = User.query.count() / size if User.query.count() % size == 0 else User.query.count() / size + 1

    # print(total)

    # users = User.query.order_by().slice((page - 1) * size, page * size)

    #

    paginate = User.query.order_by(User.uid).paginate(page=page, per_page=size, error_out=False)

    users = paginate.items

    # 总共多少条

    print(paginate.total)

    # 表示总共多少页

    print(paginate.pages)

    # 获取当前选中的页数

    print(paginate.page)

    # 如果有就返回 True 否则返回false

    print(paginate.has_prev)

    print(paginate.has_next)

    """

    <ul>

    <li><a>1<>

    <li><a>2<>

    <li><a>3<>

    <li><a>4<>

    </ul>

    left_edge =2 表示最左边2页

    """

    # paginate.iter_pages():

    return render_template('user/users.html', users=users, paginate=paginate)





# 什么是事务  指的一系列操作, 这些操作要么一起成功要么全部失败

@user.route('/save/')

def save_all():

    # db.session.save_all()

    # # insert into user (name) values('test')

    objects = []

    for i in range(1, 101):

        objects.append(User(name='test' + str(i)))

    db.session.bulk_save_objects(objects)

    # insert  into user (name) values('test1'),('test')

    db.session.commit()

    return '批量保存'





# 1>要根据条件先查询出对象

#

@user.route('/update/')

def update_one():

    # user = User.query.filter_by(name='test1').first()

    # user.name = '呵呵'

    # db.session.commit()

    User.query.filter_by(name='test1').update({'name': '呵呵'})

    db.session.commit()





# connection

# 100 + 50

@user.route('/batch/')

def batch_update():

    # User.query.filter(User.uid != 1).update({User.name: 'hehe'})

    # 表示 四则运算

    # User.query.filter(User.name == 'test1').update({User.money: User.money * 5}, synchronize_session='evaluate')

    #

    # User.query.filter(User.name == 'test1').update({User.money: User.money * 5}, synchronize_session='evaluate')

    # 表示字符串拼接

    User.query.filter(User.uid > 0).update({User.msg: '/upload' + User.msg}, synchronize_session=False)

    db.session.commit()

    return '批量更新'