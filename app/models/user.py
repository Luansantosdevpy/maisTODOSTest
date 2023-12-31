from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    confirm_password = Column(String)

    def __json__(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password
        }
