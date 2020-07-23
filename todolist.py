from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
from sqlalchemy.orm import sessionmaker

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

Session = sessionmaker(bind=engine)
session = Session()
session.commit()


def show_tasks():
    rows = session.query(Table).all()
    if len(rows) == 0:
        print("Nothing to do!")
        print()
    else:
        print("Today:")
        for idx, row in enumerate(rows):
            print(str((idx + 1)) + ") " + row.task)
        print()

def add_task():
    print("Enter task")
    task = input()
    new_row = Table(task=task)
    session.add(new_row)
    session.commit()
    print("The task has been added")
    print()


def print_menu():
    print("1) Today's tasks")
    print("2) Add task")
    print("0) Exit")
    print()


while True:
    print_menu()
    action = input()

    if action == "1":
        show_tasks()
    elif action == '2':
        add_task()
    elif action == '0':
        break
