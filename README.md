# Revature Project 0: Rev Library Lookup
A digital library cli application in python to practice connectivity with MySQ. The data is a collection of books along with meta data about each book such as title, author, publisher, etc. Python was used for data formatting before insertion into the MySQL database. The application allows the user to query the db for a READ ONLY view of the books and their related information.

### How to Run
After cloning the repository, run the following file:
```
py src/main/app.py
```
To do a hard reset, do the following:
1. Delete the books_updated.csv file within the data/out directory.
2. Format the book.csv file to accommodate for empty columns by running:
```
py src/main/format_books.py 
```
3. Load the data to your local MySQL Database by running:  
(Check the file for the database connection configuration!)
```
py src/main/load_books.py 
```
4. Finally, run the main app python file listed at the top like normal.   
### Fake Login Credentials
```
username: admin
password: password
```
### Software Stack
Software | Version#
-------- | --------
Python | v. 3.9.7
MySQL | v. 8.0.25
MySQL Workbench | v. 8.0.25
Pycharm | v. 2021.2.1