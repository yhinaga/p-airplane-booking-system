# CS425-Final-Project

## Dependencies
Psycopg -- Postgre
'pip install psycopg2'

PySide2
'pip install PySide2'

flask -- Backend Framework
'pip install flask'

SQL Alchemy -- Helps flask connect to the database
'pip install SQLAlchemy'

# Usage
## Setting up the environment variable
Set your environment variable 'FLASK_APP' equal to the 'finalProject.py' file

### For Windows (PowerShell):
- $env:FLASK_APP = 'finalProject.py' 

### For Macs (zsh):
- %export FLASK_APP=finalProject
- %flask run


## Executing
Simply execute the command: 'flask run' from the directory in which finalProject.py file is located


Execute python file in src (for now)

## Files
- ***data***
	- airplane-data.sql: Sample data file for the database
	- airplane.sql: DDL file for the database
	- old.sql/test-data.sql/test.sql: test files that are trivial to the project
- ***design***
	- Airplane ER.png: ER diagram for the project
	- Airplane Relational Schema.png: Relational schema for the project in diagram
	- relational_schema.sql: Relational schema for the prject in sql script
- ***README.md***: this document
- ***src***;
	- ***__pycache__***: File that contains necesssary documents for running flask
	- database.py: Python document that includes basic database manipulation functions.
	- finapProjec.py: Python document that creats the flask app
	- pages.py: Python document for the back-end of the application
	- ***static***: File that includes front-end styles such as CSS files, JavaScript files
	- ***templates***: File that includes HTML files for the application