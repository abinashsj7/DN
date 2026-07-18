from fastapi import FastAPI

app = FastAPI()

employees = [
    {"id": 1, "name": "John", "department": "HR"},
    {"id": 2, "name": "Emma", "department": "IT"},
    {"id": 3, "name": "David", "department": "Finance"}
]

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI Employee API"}

@app.get("/employees")
def get_employees():
    return employees

@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
    return {"message": "Employee not found"}
