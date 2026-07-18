import { useState, useEffect } from "react";
import Student from "./Student";

function App() {
  const [students] = useState([
    { id: 1, name: "Abinash", department: "CSE" },
    { id: 2, name: "Rahul", department: "IT" },
    { id: 3, name: "Priya", department: "ECE" }
  ]);

  useEffect(() => {
    console.log("Student Management App Loaded");
  }, []);

  return (
    <div>
      <h1>Advanced Student Management</h1>

      {students.map((student) => (
        <Student
          key={student.id}
          name={student.name}
          department={student.department}
        />
      ))}
    </div>
  );
}

export default App;
