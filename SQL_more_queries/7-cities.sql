-- 7-cities.sql
-- This script creates the database 'hbtn_0d_usa' and the table 'cities'
-- The table 'cities' has columns:
-- id INT, primary key, unique, auto-increment, NOT NULL
-- state_id INT, NOT NULL, FOREIGN KEY referencing states(id)
-- name VARCHAR(256) NOT NULL
-- If the database or table already exists, the script will not fail

-- Create database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database
USE hbtn_0d_usa;

-- Create table if it does not exist
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    CONSTRAINT fk_state FOREIGN KEY (state_id) REFERENCES states(id)
);
