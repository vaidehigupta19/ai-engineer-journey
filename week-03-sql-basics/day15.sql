-- Day 15 — SQL Basics
-- Run schema_setup.sql first. All queries below use the employees/departments tables.
--
-- Goal: get comfortable with SELECT, WHERE, ORDER BY, LIMIT, DISTINCT,
-- and comparison operators.


-- TODO 1: select just the name and hire_date of every employee, ordered by
--         hire_date (oldest first)
SELECT name, hire_date
FROM employees
ORDER BY hire_date ASC;

-- TODO 2: select employees hired after '2023-01-01'
SELECT *
FROM employees
WHERE hire_date > '2023-01-01';


-- TODO 3: select employees NOT in department_id 1
--         (try it with != first, then rewrite 1using NOT)
SELECT name FROM employees WHERE department_id!=1;
SELECT name FROM employees WHERE NOT department_id =1;

-- TODO 4: select employees with a salary BETWEEN 60000 AND 80000
SELECT name, salary
FROM employees
WHERE salary BETWEEN 60000 AND 80000;

-- TODO 5: select employees whose name starts with 'A'
--         (hint: LIKE and the % wildcard)
SELECT name
FROM employees
WHERE name LIKE 'A%';


-- TODO 6: select the DISTINCT department_ids that actually have employees
--         — before running it, guess how many you'll get back, given
--         department 5 (Finance) has zero employees
SELECT DISTINCT department_id
FROM employees;


-- TODO 7: select employees where department_id IS NULL
--         (note: this is why you can't write `department_id = NULL` —
--         say out loud why that comparison never works, then check
--         if your guess was right)
SELECT name
FROM employees
WHERE department_id IS NULL;

-- Self-check: close this file, open a blank one, and write TODO 3 and
-- TODO 7 from memory. Those two (NOT vs !=, and NULL comparisons) are
-- the ones people misremember most.