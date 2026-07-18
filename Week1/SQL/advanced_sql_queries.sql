-- Create Table
CREATE TABLE Employee (
    EmpID INT PRIMARY KEY,
    Name VARCHAR(50),
    Department VARCHAR(50),
    Salary INT
);

-- Insert Data
INSERT INTO Employee VALUES (1,'Alice','HR',40000);
INSERT INTO Employee VALUES (2,'Bob','IT',60000);
INSERT INTO Employee VALUES (3,'Charlie','Finance',55000);

-- Display all records
SELECT * FROM Employee;

-- Employees with salary > 50000
SELECT * FROM Employee
WHERE Salary > 50000;

-- Employees in IT
SELECT * FROM Employee
WHERE Department='IT';

-- Average salary
SELECT AVG(Salary) FROM Employee;

-- Maximum salary
SELECT MAX(Salary) FROM Employee;

-- Minimum salary
SELECT MIN(Salary) FROM Employee;

-- Count employees
SELECT COUNT(*) FROM Employee;

-- Sort by salary
SELECT * FROM Employee
ORDER BY Salary DESC;

-- Update salary
UPDATE Employee
SET Salary=65000
WHERE EmpID=2;

-- Delete employee
DELETE FROM Employee
WHERE EmpID=3;
