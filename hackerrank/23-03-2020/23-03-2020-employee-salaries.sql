-- https://www.hackerrank.com/challenges/salary-of-employees/problem
-- MS SQL
-- Write a query that prints a list of employee names (i.e.: the name attribute) for employees in Employee
-- having a salary greater than  per month who have been employees for less than  months.
-- Sort your result by ascending employee_id.

SELECT name FROM Employee WHERE months < 10 AND salary > 2000 ORDER BY employee_id;

