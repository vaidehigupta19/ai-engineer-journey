-- Shared schema for all of Week 3 (Days 15-19).
-- Run this once first — paste into db-fiddle.com (choose SQLite or MySQL),
-- or locally: sqlite3 week3.db < schema_setup.sql
 
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;
 
CREATE TABLE departments (
    department_id   INTEGER PRIMARY KEY,
    department_name TEXT NOT NULL
);
 
CREATE TABLE employees (
    employee_id   INTEGER PRIMARY KEY,
    name          TEXT NOT NULL,
    department_id INTEGER,               -- NULL = no department assigned yet
    salary        REAL NOT NULL,
    hire_date     TEXT NOT NULL,
    manager_id    INTEGER,               -- NULL = no manager (references employees.employee_id)
    FOREIGN KEY (department_id) REFERENCES departments(department_id),
    FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
);
 
INSERT INTO departments VALUES
    (1, 'Engineering'),
    (2, 'Sales'),
    (3, 'Marketing'),
    (4, 'HR'),
    (5, 'Finance');          -- zero employees on purpose — useful for JOIN practice
 
INSERT INTO employees VALUES
    (101, 'Asha Verma',  1, 95000, '2023-01-15', NULL),
    (102, 'Ravi Kumar',  1, 78000, '2023-03-10', 101),
    (103, 'Meera Nair',  1, 82000, '2022-11-01', 101),
    (104, 'Sanjay Rao',  2, 65000, '2023-06-20', NULL),
    (105, 'Priya Singh', 2, 61000, '2023-07-01', 104),
    (106, 'Karan Mehta', 2, 59000, '2024-01-10', 104),
    (107, 'Divya Iyer',  3, 71000, '2023-02-14', NULL),
    (108, 'Arjun Das',   3, 68000, '2023-09-05', 107),
    (109, 'Neha Joshi',  NULL, 55000, '2024-02-01', NULL),   -- no department (JOIN edge case)
    (110, 'Vikram Shah', 1, 99000, '2021-05-19', 101),
    (111, 'Anita Roy',   4, 60000, '2023-04-11', NULL),
    (112, 'Rohan Gupta', 2, 73000, '2022-08-23', 104);
 
-- Notes for later days:
--   * Neha Joshi has no department_id -> tests LEFT/RIGHT JOIN behavior
--   * Finance (dept 5) has no employees -> same, from the other side
--   * manager_id references employee_id in the SAME table -> self-join material
 