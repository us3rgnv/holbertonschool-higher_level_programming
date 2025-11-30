-- 1-create_user.sql
-- This script creates the MySQL server user 'user_0d_1'
-- If the user already exists, the script will not fail
-- The user will have all privileges and the password will be 'user_0d_1_pwd'

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
