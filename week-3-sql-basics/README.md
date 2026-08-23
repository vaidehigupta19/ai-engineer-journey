# Week 3 — SQL

Part of my [AI Engineer Roadmap](../README.md) — Phase 1: Foundations.

**Duration:** Day 15–21 | **Phase:** Phase 1 – Foundations | **Focus:** SQL

## 🎯 Goal for the week
Go from "never written a query" to comfortable pulling, aggregating, joining, and ranking data with SQL — the standard interface for structured data in almost every data/ML role.

## 📅 Day-by-day log

### Day 15 — SQL Basics
- Environment setup: db-fiddle.com or local MySQL
- `SELECT`, `FROM`, `WHERE`, `AND`, `OR`, `NOT`
- `ORDER BY`, `LIMIT`, `DISTINCT`
- Comparison operators: `=`, `<>`, `>`, `<`, `BETWEEN`, `IN`, `LIKE`

### Day 16 — Aggregation + Grouping
- `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`
- `GROUP BY` and `HAVING`
- Aliases with `AS`
- **Practice:** 5 SQL problems on HackerRank (Basic Select section)

### Day 17 — JOINs
- `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `FULL OUTER JOIN`
- Self joins
- Joining 3+ tables
- **Practice:** 5 JOIN problems on HackerRank

### Day 18 — Subqueries + CTEs
- Subqueries in `WHERE`, `FROM`, and `SELECT`
- Common Table Expressions (`WITH ... AS`)
- `CASE WHEN` statements
- **Practice:** 5 intermediate SQL problems on HackerRank

### Day 19 — Window Functions
- `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`
- `LAG()` and `LEAD()`
- `PARTITION BY`
- Running totals with `SUM() OVER()`

### Day 20–21 — Weekend: SQL Practice Sprint
- 15 SQL problems on HackerRank across all difficulty levels — focused on JOINs, GROUP BY, window functions, subqueries
- 3 interview-style problems on StrataScratch
- Built a personal SQL cheat sheet in my own words

## 🧠 Key takeaways


## ✅ Checkpoint
By the end of this week I could write SQL queries using filtering, aggregation, multiple types of joins, subqueries/CTEs, and window functions — enough to handle most data-analyst-level SQL interview questions.

## 📂 Files in this folder
| File | Description |
|------|-------------|
| `schema_setup.sql` | Shared employees/departments schema used by every file below — run this first |
| `day15_sql_basics.sql` | SELECT, WHERE, ORDER BY, LIMIT, DISTINCT |
| `day16_aggregation_grouping.sql` | COUNT/SUM/AVG/MIN/MAX, GROUP BY, HAVING |
| `day17_joins.sql` | INNER/LEFT/RIGHT/FULL OUTER, self joins |
| `day18_subqueries_ctes.sql` | Subqueries, CTEs, CASE WHEN |
| `day19_window_functions.sql` | RANK, DENSE_RANK, LAG/LEAD, running totals |



