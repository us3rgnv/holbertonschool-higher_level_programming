# 0. My Privileges!

## Description
This script lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on `localhost`.

## Requirements
- MySQL server must be installed and running.
- You must have root or sufficient privileges to view grants of other users.

## Usage
```bash
cat 0-privileges.sql | mysql -hlocalhost -uroot -p
