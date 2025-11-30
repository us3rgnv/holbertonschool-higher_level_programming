-- 4-first_table.sql
-- This script creates a table called first_table in the current database
-- It will not fail if the table already exists

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
