# from user import db
# class User(db.Model):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer,primary_key=True)
#     username = db.Column(db.String(64),index=True,unique=True)
#     email = db.Column(db.String(120),index=True,unique=True)
#     password_hash = db.Column(db.String(128))
#
#     def __repr__(self):
#         return '<用户名:{}>'.format(self.username)


import datetime

from app.ext import db


# 约束
# 主键约束  唯一约束  非空约束  默认约束
# 外键约束 关联关系

# 常用的数据类型
# 数字相关
# 字符串
# 日期时间
# 大文本  二进制数据

# 1000.00
# 100000

class User(db.Model):
    # __tablename__ = 't_user'
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=True)
    weight = db.Column(db.Float(10, 2))
    # # decimal
    money = db.Column(db.Numeric(10, 2))
    create_date = db.Column(db.DateTime, default=datetime.datetime.now())
    # # 不要在text字段上面加索引
    msg = db.Column(db.Text())


#    外键

# 1>在主表建立外键连接的关系
# 2>在子表建立外键
class Cate(db.Model):
    cid = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(64), index=True, unique=True, nullable=True)
    # 建立关联关系的对象
    shops = db.relationship('Shop')


class Shop(db.Model):
    sid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=True)
    # 类名小写.关联字段
    cid = db.Column(db.Integer, db.ForeignKey('cate.cid'))