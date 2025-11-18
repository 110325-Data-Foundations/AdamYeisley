-- BASIC CHALLENGES

-- List all customers (full name, customer id, and country) who are not in the USA
SELECT first_name, last_name, customer_id, country FROM customer WHERE country <> 'USA';

-- List all customers from Brazil
SELECT * FROM customer WHERE country = 'Brazil';

-- List all sales agents
SELECT * FROM employee WHERE title = 'Sales Support Agent';

-- SELECT * FROM employee WHERE title LIKE '%Agent%;
SELECT * FROM employee WHERE title LIKE '%Agent';

-- Retrieve a list of all countries in billing addresses on invoices
SELECT billing_country FROM invoice;

-- Retrieve how many invoices there were in 2009, and what was the sales total for that year?
SELECT 
COUNT(*) AS invoice_count,
SUM(total) AS sales_total
FROM invoice
WHERE invoice_date >= '2009-01-01' AND invoice_date < '2010-01-01';

-- (challenge: find the invoice count sales total for every year using one query)


-- how many line items were there for invoice #37
SELECT COUNT(*) AS line_item_count
FROM invoice_line WHERE invoice_id = 37;

-- how many invoices per country? BillingCountry  # of invoices 
SELECT COUNT(*) AS invoices_per_country 
FROM 


-- Retrieve the total sales per country, ordered by the highest total sales first.

-- JOINS CHALLENGES
-- Every Album by Artist


-- (inner keyword is optional for inner join)

-- All songs of the rock genre


-- Show all invoices of customers from brazil (mailing address not billing)


-- Show all invoices together with the name of the sales agent for each one


-- Which sales agent made the most sales in 2009?


-- How many customers are assigned to each sales agent?


-- Which track was purchased the most in 2010?


-- Show the top three best selling artists.


-- Which customers have the same initials as at least one other customer?


-- Which countries have the most invoices?


-- Which city has the customer with the highest sales total?


-- Who is the highest spending customer?


-- Return the email and full name of of all customers who listen to Rock.


-- Which artist has written the most Rock songs?


-- Which artist has generated the most revenue?




-- ADVANCED CHALLENGES
-- solve these with a mixture of joins, subqueries, CTE, and set operators.
-- solve at least one of them in two different ways, and see if the execution
-- plan for them is the same, or different.

-- 1. which artists did not make any albums at all?


-- 2. which artists did not record any tracks of the Latin genre?


-- 3. which video track has the longest length? (use media type table)



-- 4. boss employee (the one who reports to nobody)


-- 5. how many audio tracks were bought by German customers, and what was
--    the total price paid for them?



-- 6. list the names and countries of the customers supported by an employee
--    who was hired younger than 35.
