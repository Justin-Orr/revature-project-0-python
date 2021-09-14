def printLoginPrompt():
    print("___________")
    print("Rev Library")

def printWelcomeMessage():
    print("***********************************************")
    print("Welcome back to the Rev Library Lookup. You can search for books within our library. Listed below are your available commands:")
    print("***********************************************")

def printHelp():
    print("\nAvailable commands:" + "\nhelp" + "\nsearch" + "\nquit\n")


def printSearchMenuPrompt():
    print("Search for books based on one of the four attributes: title, author, genre, or publisher")
    printSearchMenuHelp()

def printSearchMenuHelp():
    print("\nAvailable commands:" + "\ntitle" + "\nauthor" + "\ngenre" + "\npublisher" + "\nhelp" + "\nback\n")
    printSearchMenuExample()

def printSearchMenuExample():
    print("Example Search:")
    print("search_attribute>: title")
    print("title>: Data Smart")
    print("\nResults:")
    print("Title: Data Smart | Author: John Foreman | Genre: data_science | Pages: 235 | Publisher: Wiley\n")