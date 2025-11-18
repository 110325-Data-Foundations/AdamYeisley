-- This is a comment in SQL

/*

SQL has multiple statement/query families.

Statement - Declare something about the shape of the data, or the database schema (users, roles, rtc.)
Query - Returning data... but also altering the data in a table

Within SQL there are some "sub-languages" or "sub-families" of commands.

DQL - Data Query Language - SELECT (and its associated keywords)
DML - Data Manipulation Language - INSERT, UPDATE, DELETE
DDL - Data Definition Language - CREATE, DROP, RENAME, TRUNCATE
TCL - Transaction Control Language - START/BEGIN TRANSACTION, COMMIT, ROLLBACK, SAVEPOINT
DCL - Data Control Language - GRANT, REVOKE 

*/

-- We are going to start with DQL - SELECT!
-- SELECT (what you want to select) FROM (table);

SELECT * FROM actor;

-- We can select specific columns too

SELECT actor_id, first_name FROM actor;

-- Limiting returns

SELECT * FROM album LIMIT 10;

-- Notice in our album table, we have album and artis id
-- In the salbum tbale album_id is the PRIMARY KEY - allows us to uniquely identify a record in this table.
-- Everytable needs a primary key, the must be unique and not null

-- In the album table, artist_id is a FOREIGN KEY
-- In SQL there are 1:1, 1:many, and many:many

-- Filtering and sorting on SELECTs
-- If we want more than just filtering by returned caloumns or limiting returned rows, we need to
-- use things like the WHERE clause

SELECT * FROM genre;

SELECT name, composer, genre_id FROM Track
WHERE genre_id = 1; -- Filtering for every rock track

-- We can combine clauses, lets use ORDER BY

SELECT name, milliseconds 
FROM track
WHERE genre_id = 1
ORDER BY milliseconds DESC
LIMIT 10;


-- AND; both conditions must be met
-- OR; one condition met
SELECT name, milliseconds
FROM Track
WHERE genre_id = 1 and milliseconds > 500000;

-- we can do pattern matching with LIKE (and regex)

SELECT customer_id, first_name, email
FROM customer
WHERE email LIKE '%@gmail.com';

-- Scalar Functions
-- Operate on a single value
-- upper(), lower(), length(), round()

-- Aggregate Functions
-- Operate over a set of values
-- count(), sum(), min(), max()

-- Basic Aggregation agains tracks table
SELECT COUNT(*), AVG(milliseconds) AS track_length -- Alias
FROM track;

-- We can create summary rows for each genre_id 
-- to see which genres have the most tracks
-- we can do this using GROUP BY

SELECT genre_id, count(*) as track_count
FROM track
GROUP BY genre_id
HAVING count(*) > 100                     -- HAVING is like WHERE, but for grouped results
ORDER BY track_count DESC;

-- Joins and Subqueries

/*
Returning data across multiple tables
You could run individual selescts and cross refrence manually, but that's not efficent
and we're not returning everything as a descrete set of data
*/

-- I want to return the album title and artist name of every album

-- Inner join (default when using just JOIN) - only records that match are returned
SELECT a.title AS album, ar.name AS artist
FROM album AS a
INNER JOIN artist ar ON a.artist_id = ar.artist_id;

-- Left and Right Joins
-- These are mirrors of each other, your left table is the first table you select (next to FROM)
-- The right table is the second one selected (after the JOIN)

-- LEFT JOIN - All record from the left table + matches from the right
SELECT ar.name, a.title
FROM artist ar
LEFT JOIN album a on ar.artist_id = a.artist_id
WHERE ar.name LIKE 'A%';

-- RIGHT JOIN - Same as left, but right table + matches from the left

-- OUTER JOIN

-- FULL OUTER JOIN returns all rows from both tables, matches records, 
-- shows null for no match, essentially a complete union of both tables

SELECT ar.name, a.title
FROM artist ar
FULL OUTER JOIN album a on ar.artist_id = a.artist_id

-- CROSS JOIN - Cartesian Product
SELECT g.name as genre, mt.name as media_type
FROM genre g
CROSS JOIN media_type mt
WHERE g.name IN ('Rock','Jazz')

SELECT * FROM genre;

