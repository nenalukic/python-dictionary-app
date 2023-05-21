# Dictionary App

This program is a dictionary where you can add a new word and its translation to the list. You can also save and delete words.

To use this program, you will need a database. You can create one using PostgreSQL.

Here's how you can get started:
- Login to the database: `psql postgres postgres`
- Create a new database: `create database dict;`
- Create a user: `create user dict with password 'abc123';`
- Grant user rights: `grant all privileges on database dict to dict;`
- Logout: `\q`

- Login to the new database: `psql dict dict`

After that, open the terminal and run `python dict.py` to start the program.