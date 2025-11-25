-- Yesterday we went through beginner to intermediate/advanced DQL

/*
Transactions and TCL

We use complex operations to ensure all commands execute, or no changes are persisted

Before creating transactions, we go over ACID

ACID - 
    Atomicity - this operation can't be broken down any further, all parts of our transaction must succeed, or they all fail
    Consistency - database moves from one valid state to another
    Isolation - transactions can't interfere or step on each other
    Durability - once a transaction is committed, changes are permanent
*/

-- Lets model a transaction inside our chinookdb
-- Example: transfer a track between playlists

-- Starts a transaction block, all following statements belong to it
BEGIN TRANSACTION;

-- remove the track from one playlist
DELETE FROM playlist_track
WHERE playlist_id = 1 AND track_id = 1;

SAVEPOINT deleted_track;

-- add the track to another playlist
INSERT INTO playlist_track (playlist_id, track_id)
VALUES(2, 1);

SAVEPOINT imported_track;


-- verify our changes before we commit
SELECT * FROM playlist_track
WHERE track_id = 1 AND playlist_id IN (1, 2);

ROLLBACK to deleted_track;

COMMIT;

/*

Indexes in SQL are like indexes in a book, they help find data faster
There are costs, the increase storage space and make writes slower


*/

-- Basic SELECT with no INDEX
EXPLAIN ANALYZE
SELECT * FROM track
WHERE composer LIKE '%John%'

-- Create index to speed it up
CREATE INDEX idx_tracks_composer ON track(composer);
EXPLAIN ANALYZE
SELECT * FROM track
WHERE composer LIKE '%John%'

-- Need to compare muiltiple columns? USe a MUilti-column index

CREATE INDEX IDX_INVOICE_CUSTOMER_TOTAL ON invoice(customer_id, total);

EXPLAIN ANALYZE
SELECT * FROM invoice
WHERE customer_id = 1 AND total > 5;

/*
Views - saved queries that we can re-use

views are virtual tables based on saved queries
We can then reues the result set as if it was a table - even within other queries
*/

CREATE OR REPLACE VIEW rock_tracks_view AS
SELECT 
    t.track_id,
    t.name as track_name,
    a.title as album_title,
    ar.name as artist_name,
    t.milliseconds,
    t.unit_price
FROM track t
JOIN album a ON t.album_id = a.album_id
JOIN artist ar ON a.artist_id = ar.artist_id
JOIN genre g ON t.genre_id = g.genre_id
WHERE g.name = 'Rock';

SELECT * FROM rock_tracks_view
WHERE album_title = 'Restless and Wild';

CREATE OR REPLACE PROCEDURE update_track_prices(
    genre_name TEXT,
    price_increase_percent 
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE track
    SET unit_price = unit_price * (1 + (price_increase_percent / 100))
    WHERE genre_id IN(
        SELECT genre_id FROM genre WHERE name = genre_name
    );

    RAISE NOTICE 'Updated Prices for % genre by %', genre_name, price_increase_percent;

END;
$$

SELECT track_name, unit_price FROM rock_tracks_view;

CALL update_track_prices('Rock', 10.0);

-- Lets create a function to get a single value back - lets do each users total money spent

CREATE OR REPLACE FUNCTION get_customer_total_spent(customer_id INTEGER)
RETURNS NUMERIC -- Return type
LANGUAGE plpgsql
AS $$

DECLARE
    total_spent NUMERIC;
BEGIN
    SELECT SUM(total) into total_spent
    FROM invoice
    WHERE customer_id = customer;
    RETURN total_spent; -- RETURNS UP TOP, RETURN BELOW
END;
$$;

-- If we want to use our function, can can SELECT it.

SELECT first_name, get_customer_total_spent(customer_id) as total_spent
FROM customer;

/*

    Triggers - A stored procedure in a db that happens auto when a specific event occurs

    Triggers can be set up to auto run on things like INSERT, UPDATE, DELETE, etc.

    Can be useful for logging, task auto, etc.
 

*/





/*

1NF - The key
2NF - The whole key
3NF - Nothing but the key

*/