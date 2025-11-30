-- 2-create_read_user.sql
-- This script creates the database 'hbtn_0d_2' and the user 'user_0d_2'
-- The user will have only SELECT privilege on hbtn_0d_2
-- If the database or user already exists, the script will not fail

-- Create database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on hbtn_0d_2 to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;
