import { useState } from "react";

function App() {
  const [name, setName] = useState("");
  const [department, setDepartment] = useState("");

  const [students, setStudents] = useState([
    { name: "Abinash", department: "CSE" },
    { name: "Rahul", department: "IT" }
  ]);

  const addStudent = () => {
    if (name === "" || department === "") {
      alert("Please fill all fields");
      return;
    }

    setStudents([
      ...students,
      {
        name: name,
        department: department
      }
    ]);

    setName("");
    setDepartment("");
  };

  return (
    <div>
      <h1>Student Management System</h1>

      <input
        type="text"
        placeholder="Enter Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <br /><br />

      <input
        type="text"
        placeholder="Enter Department"
        value={department}
        onChange={(e) => setDepartment(e.target.value)}
      />

      <br /><br />

      <button onClick={addStudent}>
        Add Student
      </button>

      <hr />

      <h2>Students</h2>

      <ul>
        {students.map((student, index) => (
          <li key={index}>
            {student.name} - {student.department}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
