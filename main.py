# This is the entry point of the code

import pylint
from fastapi import FastAPI,HTTPException
from working_file import root, add_student
from pydantic import BaseModel


app = FastAPI()


class Student(BaseModel):
    student_id: int
    first_name: str
    last_name: str
    email: str
    gender: str
    address: str


@app.get("/{student_id}")
async def get_student_details(student_id: int):
    return await root(student_id)

@app.post("/")
async def create_student(student: Student):
    try:
        await add_student(student.dict())
        return {"student added successfully"}
    except:
        raise HTTPException(status_code=500, detail=str(e))