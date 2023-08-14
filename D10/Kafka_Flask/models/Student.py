from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


engine = create_engine('mysql+mysqlconnector://newuser1@localhost/miko_students', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.metadata.create_all(engine)  # make the tables
Base.query = db_session.query_property()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    age = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'age': self.age}

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', age='{self.age}', created_at='{self.created_at}', updated_at='{self.updated_at}')>"

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)