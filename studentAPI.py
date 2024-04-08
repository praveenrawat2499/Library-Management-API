from fastapi import FastAPI, HTTPException, Query
from pymongo import MongoClient
from pydantic import BaseModel
from bson import ObjectId
from dotenv import load_dotenv
import os


load_dotenv()

app = FastAPI()

db_uri = os.getenv("DATABASE_URI")

# Connecting the Database
client = MongoClient(db_uri)
db = client["Library_Management"]
students_data = db["students"]


class Address(BaseModel):
    city : str
    country : str

class Student(BaseModel):
    name : str
    age : int
    address : Address
    

# Creating Routes

# Create_Student : Creates the entry of newly created student in the database.
@app.post("/students", response_model=dict)
def Create_Student(student: Student):
    student_data = student.model_dump()
    result = students_data.insert_one(student_data)
    return {"id" : str(result.inserted_id)}


# List_Students : Show all the student based on their country or age.
@app.get("/students", response_model = dict)
def List_Students(country: str = Query(None), age: int=Query(None)):
    filtered = {}
    if country:
        filtered["address.country"] = country 
    if age:
        filtered["age"] = {"$gte":age}
    students = list(students_data.find(filtered, {"_id" : 0}))
    return {"data" : students}


# Get_Students : It returns the details of a student by their id.
@app.get("/students/{id}", response_model = Student)
def Get_Students(id:str):
    student = students_data.find_one({"_id" : ObjectId(id)}, {"_id":0})
    if student:
        return student
    raise HTTPException(status_code=404, detail="Student Not Found")


# Update_Student : It updates the student details in the Database by their id.
@app.patch("/students/{id}", response_model=dict)
def Update_Student(id:str, student:Student):
    updated_Data = student.model_dump(exclude_unset=True)
    updated_student = students_data.update_one({"_id":ObjectId(id)}, {"$set":updated_Data})
    if updated_student.modified_count == 1:
        return {}
    raise HTTPException(status_code=404, detail="Student Not Found")


# Delete_Student : It deletes the data of the student from the database based on their id.
@app.delete("/students/{id}", response_model=dict)
def Delete_Student(id: str):
    deleted_student = students_data.delete_one({"_id": ObjectId(id)})
    if deleted_student.deleted_count == 1:
        return {}
    raise HTTPException(status_code=404, detail="Student not found")
