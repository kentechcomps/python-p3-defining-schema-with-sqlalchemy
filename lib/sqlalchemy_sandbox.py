#!/usr/bin/env python3
from datetime import datetime

from sqlalchemy import (create_engine, desc,
    CheckConstraint, PrimaryKeyConstraint, UniqueConstraint,
    Index, Column, DateTime, Integer, String , func)

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):

    __tablename__ = 'students'

    __table_args__ = (
        PrimaryKeyConstraint(
            'id',
            name='id_pk'),
        UniqueConstraint(
            'email',
            name='unique_email'),
        CheckConstraint(
            'grade BETWEEN 1 AND 12',
            name='grade_between_1_and_12')
    )

    Index('index_name', 'name')

    id = Column(Integer())
    name = Column(String())
    email = Column(String(55))
    grade = Column(Integer())
    birthday = Column(DateTime())
    enrolled_date = Column(DateTime(), default=datetime.now())

def __repr__(self):
        return f"Student {self.id}: " \
            + f"{self.name}, " \
            + f"Grade {self.grade}"


if __name__ == '__main__':
      engine = create_engine('sqlite:///sqlalchemy.db')
      Base.metadata .create_all(engine)

    # use our engine to configure a 'Session' class
      Session = sessionmaker(bind=engine)
    # use 'Session' class to create 'session' object
      session = Session()

      albert_einstein =  Student(
        name="Albert Einstein",
        email="albert.einstein@zurich.edu",
        grade=6,
        birthday=datetime(
            year=1879,
            month=3,
            day=14
        ),
    )
      
      alan_turing = Student(
        name="Alan Turing",
        email="alan.turing@sherborne.edu",
        grade=11,
        birthday=datetime(
            year=1912,
            month=6,
            day=23
        ),
    )
      
      KennedyMutuku = Student(
        name="Kennedy Mutuku",
        email="mutukukennedy@gmail.com",
        grade=12,
        birthday=datetime(
            year=1913,
            month=6,
            day=23
        ),
    )



      #if there are multiple objects you want to save at once it is advisable you use
      session.bulk_save_objects([albert_einstein ,alan_turing , KennedyMutuku ])
      #if you want to save a single record
      #session.add(albert_einstein)
      session.commit()
       #return all records
      students = session.query(Student).all()
      #return specific columns
      names = [name for name in session.query(Student.name)]

      #ordering in a specific way
      students_by_grade_desc = [student for student in session.query(
            Student.name, Student.grade).order_by(
            desc(Student.grade))]
      #limitinf
      students_by_grade_desc = [student for student in session.query(
            Student.name, Student.birthday).order_by(
            desc(Student.grade)).first()]

      #the func method from sqlalchemy gives us access to common SQL operation
      student_count = session.query(func.count(Student.id)).first()

      print(student_count)

      print(names)

      print( students)

      print(f"New student ID is {albert_einstein.id}.")
      print(f"New student ID is {alan_turing.id}.")



      #updatingdata

      session.query(Student).update({
            Student.grade: Student.grade + 1
      })
      print([(
            student.name ,
            student.grade
      ) for student in session.query(Student)])

#deleting records
      query = session.query(
        Student).filter(
            Student.name == "Albert Einstein")        

    # retrieve first matching record as object
      albert_einstein = query.first()

    # delete record
      session.delete(albert_einstein)
      session.commit()

    # try to retrieve deleted record
      albert_einstein = query.first()
  
      print(albert_einstein)

