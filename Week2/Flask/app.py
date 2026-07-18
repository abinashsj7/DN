from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "Alice", "department": "CSE"},
    {"id": 2, "name": "Bob", "department": "ECE"},
    {"id": 3, "name": "Charlie", "department": "IT"}
]


@app.route("/")
def home():
    return "Welcome to Flask Student API"


@app.route("/students")
def get_students():
    return jsonify(students)


@app.route("/students/<int:id>")
def get_student(id):
    for student in students:
        if student["id"] == id:
            return jsonify(student)
    return jsonify({"message": "Student not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
