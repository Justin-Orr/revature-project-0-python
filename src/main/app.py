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

    # Test Database connection
    print("-- Testing Database Connection --")
    cnx = mysql.connector.connect(user='root', password='Ro93Jo98@', host='127.0.0.1', database='demodatabase')
    cnx.close()

main()