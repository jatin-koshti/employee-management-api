from fastapi import FastAPI
from app.database import employees

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Employee API Running"}

@app.get("/employees")
def get_employees():
    data = []

    for emp in employees.find():
        emp["_id"] = str(emp["_id"])
        data.append(emp)

    return data