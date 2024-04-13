# FastAPI-Student-Data-Endpoint
This FastAPI application provides an endpoint to fetch and modify student data based on the student ID from a JSON file.


**Prerequisites**

Python 3.x

FastAPI

Uvicorn (optional, for running the application)

**Installation**

Clone the repository:

`git clone https://github.com/nehajalan13/FastAPI-Student-Data-Endpoint`

`cd your-repo`

Install dependencies:

`pip install fastapi uvicorn`

Start the FastAPI application:

`uvicorn main:app --reload`

The application will start running at http://localhost:8000.

To get student details, send a GET request to /student_id, where student_id is the ID of the student you want to fetch.

Example:
curl http://localhost:8000/32

To add a new student, send a POST request to /student_id with a JSON payload containing the student's details.

Example:

curl -X POST -H "Content-Type: application/json" -d '{"student_id": 34, "first_name": "New", "last_name": "Student", "email": "new@student.com", "gender": "Male", "address": "123 Street"}' http://localhost:8000/34

**JSON Data Format**

The JSON file (Data.json) should contain student data in the following format:

[

    {
    
        "student_id": 31,
        
        "first_name": "Florenza",
        
        "last_name": "Labbet",
        
        "email": "flabbetu@ucoz.ru",
        
        "gender": "Female",
        
        "address": "Apt 1144, Pin - 357668"
        
    },
    
    {
    
        "student_id": 32,
        
        "first_name": "Hall",
        
        "last_name": "Sudy",
        
        "email": "hsudyv@yale.edu",
        
        "gender": "Male",
        
        "address": "Suite 42, Pin - 674678+"
        
    },
    
    {
    
        "student_id": 33,
        
        "first_name": "Lenci",
        
        "last_name": "Cunnane",
        
        "email": "lcunnanew@umn.edu",
        
        "gender": "Male",
        
        "address": "Apt 672"
        
    }
]

**Endpoint Details**

GET /student_id: Fetches student details based on the provided student_id.
POST /student_id: Adds a new student with the provided student_id and details to the JSON file.


**License**

This project is an open source for learning purpose.
