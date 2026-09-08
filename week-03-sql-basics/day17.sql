-- Day 17 — JOINs
-- Run schema_setup.sql first.
--
-- Goal: combine rows from employees and departments (and employees with
-- itself) based on matching keys.

-- Worked example (LEFT JOIN — keeps every employee, even Neha with no dept):
SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id;

-- TODO 1: write the same join as INNER JOIN instead of LEFT JOIN.
--         Compare row counts. Who disappeared, and why?
SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id;


-- TODO 2: write it as a RIGHT JOIN (departments on the left side of the
--         FROM instead). Which department shows up with a NULL name
--         for employee? Why?
SELECT e.name, d.department_name
FROM employees e
RIGHT JOIN departments d ON e.department_id = d.department_id;


-- TODO 3: write it as a FULL OUTER JOIN. This should show BOTH the
--         employee with no department AND the department with no
--         employees, in one result set.
SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d
    ON e.department_id = d.department_id

UNION

SELECT e.name, d.department_name
FROM employees e
RIGHT JOIN departments d
    ON e.department_id = d.department_id;

-- TODO 4: SELF JOIN — for every employee who has a manager, show the
--         employee's name next to their MANAGER's name.
--         (hint: join the employees table to itself using two aliases,
--         e.g. `emp` and `mgr`, matching emp.manager_id = mgr.employee_id)
SELECT emp.name AS employee_name, mgr.name AS manager_name
FROM employees emp
LEFT JOIN employees mgr ON emp.manager_id = mgr.employee_id;

-- TODO 5: JOIN 3+ TABLES worth of logic — since we only have two real
--         tables, simulate it: join employees to departments, AND
--         self-join employees to get the manager's name, all in one
--         query. Final columns: employee name, department name,
--         manager name.
SELECT emp.name AS employee_name, mgr.name AS manager_name,
       d.department_name
FROM employees emp
LEFT JOIN departments d ON emp.department_id = d.department_id
LEFT JOIN employees mgr ON emp.manager_id = mgr.employee_id

-- Self-check: TODO 3 (FULL OUTER) and TODO 4 (self join) are the ones
-- that don't stick on first pass for most people. Rewrite both from
-- memory before Day 18.