import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:1558785107zsh@localhost/pythonservice",
                       encoding='utf-8', )

Base = declarative_base()  # 生成orm基类


class User(Base):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return "<User(id=%s,name='%s')>" % (self.id,
            self.name)


Base.metadata.create_all(engine)  # 创建表结构

Session_class = sessionmaker(bind=engine)  #创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = Session_class() #生成session实例

# user_obj = User(name='alex',password='123456')
# print(user_obj.name,user_obj.id)
# session.add(user_obj)
# print(user_obj.name)
# session.commit()  #统一提交后创建

date = session.query(User).filter(User.id>2).filter(User.id<4).all()
print(date)


