from sqlalchemy import create_engine, Column, Integer, String, or_, and_, not_, desc, asc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///final.db', echo=True)
# create_engine('postgresql:///dakshbindal:123@localhost:5432/python_test')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    lastname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', lastname='%s')>" % (self.name, self.fullname, self.lastname)


if __name__ == '__main__':
    Base.metadata.create_all(engine)

# user_a = User(name="hello", fullname="Daksh", lastname="Bindal")
# session.add(user_a)
# session.commit()
# session.close()

# rows=session.query(User).get(1)
# rows_where=session.query(User).filter(User.name == 'hello')
# print(rows)
# print(session.query(User).filter(or_(User.name == 'hello', User.lastname.ilike('a%'))).all())
print(session.query(User).order_by(desc(User.id)).all())