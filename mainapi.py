from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

students = {
    1 : {
        'name': 'kanak',
        'age': '21',
        'year': 'final year'
    },
    2 : {
        'name': 'john',
        'age': '21',
        'year': 'third year'
    }
}

class Student(BaseModel):
    name : str
    age: int
    year : str

@app.get('/')
def index():
    return {"name": "Kanak desai"} 

@app.get('/get-student/{student_id}')
def getStudent(student_id: int):
    return students[student_id]

@app.get('/get-by-name')
def byName(name : str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {'Data': 'data not found'} 


@app.post('/add-student/{student_id}')
def addStudent(student_id: int, student : Student):
    if student_id in students:
        return {'Error': 'student already exists'}
    students[student_id]= student
    return students[student_id]