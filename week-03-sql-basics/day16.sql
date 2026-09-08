-- Day 16 — Aggregation + Grouping
-- Run schema_setup.sql first.
--
-- Goal: summarize rows into single numbers, and summarize GROUPS of rows.

-- Worked example:
SELECT department_id, AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id;

-- TODO 1: count the total number of employees (COUNT(*))
SELECT COUNT(*) AS total_employees
FROM employees;

-- TODO 2: find the MIN and MAX salary across the whole company, in one query
SELECT MIN(salary) AS min_salary, MAX(salary) AS max_salary
FROM employees;

-- TODO 3: find the total (SUM) salary cost per department
--         — use AS to alias the result column something readable
SELECT department_id, SUM(salary) AS total_salary_cost
FROM employees
GROUP BY department_id;

-- TODO 4: count how many employees are in each department
--         (careful: COUNT(department_id) vs COUNT(*) behave differently
--         when a row has a NULL department_id — try both and compare
--         the numbers before reading further)
SELECT department_id,
       COUNT(*) AS count_star,
       COUNT(department_id) AS count_col
FROM employees
GROUP BY department_id;

-- TODO 5: find departments where the AVERAGE salary is above 65000
--         (this needs HAVING, not WHERE — write down in one sentence
--         why WHERE won't work here before you try it)
SELECT department_id, AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id
HAVING AVG(salary) > 65000;

-- TODO 6: same as TODO 5, but also require the department to have at
--         least 2 employees (combine two conditions in HAVING)
SELECT department_id, AVG(salary) AS avg_salary, COUNT(*) AS emp_count
FROM employees
GROUP BY department_id
HAVING AVG(salary) > 65000 AND COUNT(*) >= 2;

