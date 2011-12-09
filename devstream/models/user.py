# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from devstream.libs.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True)
    username = Column(String(50))
    password = Column(String(50))
    created = Column(DateTime)

    def __init__(self, email, password):
        if self.created is None:
            self.created = datetime.utcnow()
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.email
