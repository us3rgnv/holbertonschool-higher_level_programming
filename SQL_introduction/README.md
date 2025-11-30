# 0. List Databases

## Description
This script lists all databases present in your MySQL server.  
It uses the `SHOW DATABASES;` command and displays them in alphabetical order.

## Requirements
- MySQL server must be installed and running.
- You must have access to a MySQL user (e.g., `root`) with privileges to list databases.

## Usage
```bash
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
