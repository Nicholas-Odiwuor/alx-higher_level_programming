# Python - Object-relational mapping

## Background Context
This project involves linking two worlds: Databases and Python!

### Part 1:
- Use the MySQLdb module to connect to a MySQL database.
- Execute SQL queries.

### Part 2:
- Utilize SQLAlchemy, an Object Relational Mapper (ORM).
- Abstract storage to usage, eliminating the need for SQL queries.
- Flexibility to change storage without rewriting the entire project.

## General
- Python programming advantages.
- Connecting to MySQL database from Python.
- Selecting rows in a MySQL table from Python.
- Inserting rows in a MySQL table from Python.
- Understanding ORM.
- Mapping a Python Class to a MySQL table.
- Creating a Python Virtual Environment.

## Copyright - Plagiarism
- Tasks must be solved independently.
- Plagiarism will result in removal from the program.

## Requirements
- Ubuntu 20.04 LTS with Python 3.8.5.
- MySQLdb version 2.0.x.
- SQLAlchemy version 1.4.x.
- Pycodestyle (version 2.8.*).
- Executable files ending with a new line.
- First line of files: `#!/usr/bin/python3`.
- Mandatory README.md file.
- Documentation for modules, classes, and functions.
- Avoid using execute with sqlalchemy.

## More Info
### Install and activate venv
```bash
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate

#Install MySQLdb module version 2.0.x
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient

#Install SQLAlchemy module version 1.4.x
$ sudo pip3 install SQLAlchemy

