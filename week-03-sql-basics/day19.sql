-- Day 19 — Window Functions
-- Run schema_setup.sql first.
--
-- Goal: rank, compare, and accumulate values ACROSS rows without
-- collapsing them into a single row (which is what GROUP BY does) —
-- this is the thing that finally makes "leaderboard" and "running
-- total" style questions easy.

-- Worked example — rank employees by salary WITHIN each department:
SELECT
    name,
    department_id,
    salary,
    RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS dept_rank
FROM employees;

-- TODO 1: same as above but with ROW_NUMBER() instead of RANK().
--         Give two employees in Engineering the exact same salary
--         (temporarily edit your data or just reason about it) and
--         predict how ROW_NUMBER and RANK would differ for a tie.
SELECT name, department_id, salary,
       ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS RN
FROM employees;

-- TODO 2: same again with DENSE_RANK(). Now you have all three —
--         write one sentence each on how RANK, DENSE_RANK, and
--         ROW_NUMBER differ when there's a tie. This is a very
--         common interview question.
SELECT name, department_id, salary,
      RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rnk,
      DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS dense_rnk,
      ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS row_num
FROM employees;

-- TODO 3: for each employee, show their salary AND the salary of the
--         next-highest-paid person in their department, using LAG()
--         or LEAD() (pick whichever direction makes sense — think
--         about which one before checking the docs)
SELECT name, department_id, salary,
       LAG(name) OVER (PARTITION BY department_id ORDER BY salary DESC) AS next_highest_paid
FROM employees;

-- TODO 4: a running total of salary, ordered by hire_date, across the
--         WHOLE company (no PARTITION BY) — this is the classic
--         "running total" pattern:
--         SUM(salary) OVER (ORDER BY hire_date)
SELECT name, hire_date, salary,
       SUM(salary) OVER (ORDER BY hire_date) AS running_total
FROM employees
ORDER BY hire_date;

-- TODO 5: a running total of salary PER DEPARTMENT, ordered by
--         hire_date — combine PARTITION BY and ORDER BY in the same
--         OVER() clause
SELECT name, department_id, hire_date, salary,
       SUM(salary) OVER (PARTITION BY department_id ORDER BY hire_date) AS dept_running_total
FROM employees
ORDER BY department_id, hire_date;

-- Self-check: before the weekend sprint, rewrite TODO 2 (the
-- RANK/DENSE_RANK/ROW_NUMBER comparison) and TODO 5 (partitioned
-- running total) from memory, no notes.