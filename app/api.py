from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import flask_app, Student, Class, db
from datetime import date

app = FastAPI()

origins = [
    'http://localhost:5173',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "OK"}

### STUDENTS ###
@app.get("/student", tags=["Student"])
def list_students(id: int = None):
    with flask_app.app_context():
        if id == None :
            return Student.query.all()
        else:
            return Student.query.get(id)

@app.post("/student", tags=["Student"])
def create_student(name: str, price: float):
    with flask_app.app_context():
        student = Student(name=name, price=price)
        db.session.add(student)
        db.session.commit()
        
        return {
            "message": "Student created",
            "name": student.name,
            "price": student.price
        }

@app.put("/student", tags=["Student"])
def update_student(id: int, name: str = None, price: float = None):
    with flask_app.app_context():
        student = Student.query.get(id)
        if student is not None:
            if name != None:
                student.name = name
            if price != None:
                student.price = price

            db.session.commit()

            return {
                "message": "Student updated",
                "name": student.name,
                "price": student.price
            }
        
        return {
            "message": "Student not found"
        }

@app.delete("/student", tags=["Student"])
def delete_student(id: int):
    with flask_app.app_context():
        student = Student.query.get(id)
        if student is not None:
            db.session.delete(student)
            db.session.commit()

            return {
                "message": "Student deleted",
                "name": student.name
            }
        
        return {
            "message": "Student not found"
        }

### CLASSES ###
@app.get("/class", tags=["Class"])
def list_classes(id: int = None, student: int = None):
    with flask_app.app_context():
        if id is not None:
            return Class.query.get(id)
        elif student is not None:
            return Class.query.filter_by(student_id=student).all()
        else:
            return Class.query.all()

@app.post("/class", tags=["Class"])
def create_class(student_id: int, price: float, time: int, date: date):
    with flask_app.app_context():
        student_class = Class(student_id=student_id, price=price, time=time, date=date)
        db.session.add(student_class)
        db.session.commit()

        return {
            "message": "Class created",
            "student": student_class.student_id,
            "price": student_class.price,
            "time": student_class.time,
            "date": student_class.date,
            "paid_date": student_class.paid_date,
            "paid": student_class.paid
        }

@app.put("/class", tags=["Class"])
def update_class(id: int, price: float = None, time: int = None, date: date = None, paid_date: date = None, paid: bool = None):
    with flask_app.app_context():
        student_class = Class.query.get(id)
        if student_class is not None:
            if price != None:
                student_class.price = price
            if time != None:
                student_class.time = time
            if date != None:
                student_class.date = date
            if paid_date != None:
                student_class.paid_date = paid_date
            if paid != None:
                student_class.paid = paid

            db.session.commit()

            return {
                "message": "Class updated",
                "student": student_class.student_id,
                "price": student_class.price,
                "time": student_class.time,
                "date": student_class.date,
                "paid_date": student_class.paid_date,
                "paid": student_class.paid
            }
        
        return {
            "message": "Class not found"
        }

@app.delete("/class", tags=["Class"])
def delete_class(id: int):
    with flask_app.app_context():
        student_class = Class.query.get(id)
        if student_class is not None:
            db.session.delete(student_class)
            db.session.commit()
            
            return {
                "message": "Class deleted"
            }
        
        return {
            "message": "Class not found"
        }
