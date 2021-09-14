import sys
import mysql.connector
from mysql.connector import errorcode
from tabulate import tabulate
from library_prompter import *
from format_books import *

username = "admin"
password = "password"

def login():
    finished = False
    while not finished:
        print("Type exit for username and leave password empty to quit program.")
        user = input("username>: ")
        pw = input("password>: ")
        if user == username and pw == password:
            print(" ")
            finished = True
        elif user == "exit":
            sys.exit()
        else:
            print("Invalid Credentials. Try again.")

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
        print("-- Connection Successful --\n")
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()

def searchMenu():
    printSearchMenuPrompt()
    finished = False
    while not finished:
        command = input("search_attribute>: ")

        if command == "title":
            queryDB("title")
        elif command == "author":
            queryDB("author")
        elif command == "genre":
            queryDB("genre")
        elif command == "publisher":
            queryDB("publisher")
        elif command == "help":
            printSearchMenuHelp()
        elif command == "back":
            finished = True
        else:
            print("Unexpected command: Type \"help\" to relist possible commands")

def queryDB(search_attribute):
    nput = input(f"{search_attribute}>: ")
    cursor = cnx.cursor()
    query = ("SELECT * FROM books WHERE " + search_attribute + " LIKE \"%" + nput + "%\"")
    cursor.execute(query)
    header = list(cursor.column_names)
    table = list()

    for result in cursor:
        table.append(result)

    print(tabulate(table, headers=header, tablefmt="pretty"))

    cursor.close()


def main():
    login()

    # For formatted table output: https://pypi.org/project/tabulate/
    global cnx
    cnx = mysql_connection()

    printWelcomeMessage()

    finished = False
    while not finished:
        printHelp()
        command = input(">: ")

        if command == "help":
            # Will print when looped, (finished set to false is to help python compile, not meant to do anything)
            finished = False
        elif command == "search":
            searchMenu()
        elif command == "quit":
            finished = True
        else:
            print("Unexpected command: Type \"help\" to relist possible commands")

    cnx.close()
    print("Closing program")
    sys.exit()


main()