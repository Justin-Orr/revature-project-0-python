import mysql.connector
from mysql.connector import errorcode
import sys
from library_prompter import *
from format_books import *

username = "admin"
password = "password"

def main():
    # Grab the runtime mode as a command line argument
    # (No argument) or 0 -> no data preprocessing
    # 1 -> Run data preprocessing code
    args = sys.argv[1:]

    if len(args) != 0 and args[0] == "1":
        # Preprocess data from data\in folder and output to data\out folder
        format_data('data\\in\\books.csv', 'data\\out\\books_updated.csv')
        print("-- Data formatting finished --")

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
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()

main()