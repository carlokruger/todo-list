from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
import datetime
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///todo.db?check_same_thread=False')


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.date.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
session.commit()


def today_tasks():
    today = datetime.date.today()
    rows = session.query(Table).filter(Table.deadline == today).all()
    print("Today " + datetime.datetime.strftime(today, '%d %b') + ":")
    if len(rows) == 0:
        print("Nothing to do!")
        print()
    else:
        for idx, row in enumerate(rows):
            print(str((idx + 1)) + ". " + row.task)
        print()


def add_task():
    print("Enter task")
    task = input()
    print("Enter deadline")
    year, month, day = input().split("-")
    year, month, day = int(year), int(month), int(day)
    new_row = Table(task=task, deadline=datetime.date(year, month, day))
    session.add(new_row)
    session.commit()
    print("The task has been added")
    print()


def weeks_tasks():
    today = datetime.date.today()
    for i in range(7):
        day = today + datetime.timedelta(days=i)
        print(datetime.datetime.strftime(day, '%A %d %b'))
        num = 1
        rows = session.query(Table).filter(Table.deadline == day).all()
        if len(rows) == 0:
            print("Nothing to do!")
        else:
            for row in rows:
                print(str(num) + ". " + row.task)
                num += 1
        print()


def all_tasks():
    rows = session.query(Table).order_by(Table.deadline).all()
    print("All tasks:")
    for idx, row in enumerate(rows):
        print(str(idx + 1) + ". " + row.task + ". " + str(datetime.datetime.strftime(row.deadline, '%d %b')))
    print()


def print_menu():
    print("1) Today's tasks")
    print("2) Week's tasks")
    print("3) All tasks")
    print("4) Add task")
    print("0) Exit")
    print()


while True:
    print_menu()
    action = input()

    if action == "1":
        today_tasks()
    elif action == '2':
        weeks_tasks()
    elif action == '3':
        all_tasks()
    elif action == '4':
        add_task()
    elif action == '0':
        break
