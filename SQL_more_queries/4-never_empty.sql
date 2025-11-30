-- 4-never_empty.sql
-- This script creates the table 'id_not_null' in the specified database
-- The table has columns:
-- id INT with default value 1
-- name VARCHAR(256)
-- If the table already exists, the script will not fail

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
