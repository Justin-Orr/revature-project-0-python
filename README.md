# Revature Project 0: Rev Library Lookup
A digital library cli application in python to practice connectivity with MySQ. The data is a collection of books along with meta data about each book such as title, author, publisher, etc. Python was used for data formatting before insertion into the MySQL database. The application allows the user to query the db for a READ ONLY view of the books and their related information.

### How to Run
After cloning the repository run the following python file with no arguments or an argument of 0:
```
py src/main/app.py
```
or
```
py src/main/app.py 0
```
To generate the formatted book data from the original file from the data/in folder, run the command below with an argument of 1.
```
py src/main/app.py 1
```
### Software Stack
Software | Version#
-------- | --------
Python | v. 3.9.7
MySQL | v. 8.0.25
MySQL Workbench | v. 8.0.25
Pycharm | v. 2021.2.1