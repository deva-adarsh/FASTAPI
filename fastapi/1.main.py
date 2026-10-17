# Path parameters:
# Path parameters let you capture values directly from the URL.
# They are the parts of the URL inside { }.

# Query parameters:
# Query parameters are the values that come after ? in the URL.
# They are often used for filters, pagination, etc.

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()


# Root endpoint
@app.get("/")
def get_root():
    return {"Message": "Hello There"}


# About endpoint
@app.get("/about")
def product_details():
    return {"product": "The details of products"}


# Path parameter + Query parameter
@app.get("/about/{name}")
def employee(name: str, age: int):  # age: Optional[int]=None makes the age None
    return {
        "Name": f"Hello {name} you are {age} years old"
    }


#POST METHOD--->create a new data in database


class Student_info(BaseModel):
    name: str
    age: int
    roll_no: int


@app.post("/create_student")
def create_info(student: Student_info):
    return {
        "name": student.name,
        "age": student.age,
        "roll_no": student.roll_no
    }


