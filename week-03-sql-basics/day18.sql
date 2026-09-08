-- Day 18 — Subqueries + CTEs
-- Run schema_setup.sql first.
--
-- Goal: use a query's result as an input to another query, and use
-- CTEs (WITH ... AS) to make multi-step logic readable.

-- Worked example — subquery in WHERE:
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- TODO 1: subquery in SELECT — for each employee, show their salary
--         AND the company-wide average salary side by side (as two
--         columns in the same row)
SELECT name, salary,
       (SELECT AVG(salary) FROM employees) AS company_avg
FROM employees;

-- TODO 2: subquery in FROM — first write a subquery that computes
--         avg_salary per department, then in the OUTER query select
--         only the departments where avg_salary is above 65000.
--         (yes, this is the same result as HAVING from Day 16 — the
--         point is to see the same problem solved a different way)
SELECT *
FROM(
    SELECT department_id, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department_id
) dept_avgs
WHERE avg_salary > 65000;

-- TODO 3: rewrite TODO 2 using a CTE instead:
--         WITH dept_avg AS (
--             ...
--         )
--         SELECT ...
--         Compare readability to TODO 2 — which would you rather debug
--         at 2am?
WITH dept_avg AS (
    SELECT department_id, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department_id
)
SELECT * FROM dept_avg
WHERE avg_salary > 65000;

-- TODO 4: CASE WHEN — add a column that labels each employee as
--         'high', 'mid', or 'low' earner based on salary thresholds
--         you choose
SELECT name, salary,
    CASE
        WHEN salary >= 80000 THEN 'high'
        WHEN salary >= 65000 THEN 'mid'
        ELSE 'low'
    END AS earner_level
FROM employees;

-- TODO 5: combine what you've learned — using a CTE, find each
--         department's average salary, then join that CTE back to
--         employees to show each employee's salary next to their
--         department's average
WITH dept_avg AS (
    SELECT department_id, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department_id
)
SELECT e.name, e.salary, d.avg_salary
FROM employees e
JOIN dept_avg d ON e.department_id = d.department_id;
-- Self-check: rewrite TODO 3 (the CTE version) from memory before
-- Day 19. CTEs are what separates "can write a query" from "can write
-- a query someone else can read."