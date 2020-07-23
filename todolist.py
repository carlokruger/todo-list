from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime

Base = declarative_base()



engine = create_engine('sqlite:///todo.db?check_same_thread=False')

class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.string_field


Base.metadata.create_all(engine)


def show_tasks():
    pass


def add_task():
    pass


while True:
    print_menu()
    action = input()

    if action == "1":
        show_tasks()
    elif action == '2':
        add_task()
    elif action == '0':
        break
