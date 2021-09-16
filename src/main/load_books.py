import csv
import sys
import mysql.connector
from mysql.connector import errorcode

def mysql_connection():
    # https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
    config = {
        'user': 'root',
        'password': 'Ro93Jo98@',
        'database': 'demodatabase',
        'auth_plugin': 'mysql_native_password'
    }

    # Test Database connection
    try:
        print("-- Testing Database Connection --")
        cnx = mysql.connector.connect(**config)
        print("-- Connection Successful --")
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("-- Connection Failed --")
            print("Something is wrong with your user name or password (Check your database configuration)\n")

        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("-- Connection Failed --")
            print("Database does not exist (Check your database configuration)\n")
        else:
            print(err)
    else:
        cnx.close()

def create_books_table():
    created = False
    table_description = """CREATE TABLE book 
    (title VARCHAR(255),
    author VARCHAR(255),
    genre VARCHAR(255),
    pages INT,
    publisher VARCHAR(255))"""
    try:
        print("Attempting to create table \"{}\": ".format("book"), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Table already exists")
        else:
            print(err.msg)
    else:
        print("Table created successfully")
        created = True

    return created

def load_books_data():
    print("Loading Books...")
    with open('../../data/out/books_updated.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        i = 0 # Used tp skip the header row
        for book_entry in csv_reader:
            if i == 0:
                i+=1
                continue
            book_data = (book_entry[0], book_entry[1], book_entry[2], book_entry[3], book_entry[4])
            query = "INSERT INTO book (title, author, genre, pages, publisher) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, book_data)
    cnx.commit()
    print("-- Books Loaded Successfully --")


def main():
    # Assumption, MySQL database is already created to create the table (Otherwise connection would not be possible
    global cnx
    global cursor
    cnx = mysql_connection()
    if cnx is None:
        print("-- Connection to Database not established: Closing Program --")
        sys.exit(1)
    cursor = cnx.cursor()

    created = create_books_table()
    if created is True:
        load_books_data()
    cursor.close()
    cnx.close()
    sys.exit()

main()