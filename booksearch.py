"""Contains all the functions needed to take data from database.py to send to menu.py"""


import database
from datetime import datetime, date


def days_between(d):
    """Return number of days between today and input date"""
    today = datetime.today()
    d = datetime.strptime(d, "%d-%m-%y")
    delta = today - d
    return abs(delta.days)



def check_overdue(bookline):
    """Take line of data from database and output a message"""
    bookline = bookline.strip()
    bookline_array = bookline.split(",")
    ID = bookline_array[0].strip()
    checkout_date_string = database.return_last_checkout_date(ID)
    if checkout_date_string == False:
        return bookline
    else:
        
        if days_between(checkout_date_string) > 60:
            return bookline + " This book is overdue!"
        else:
            return bookline + " This book is not overdue"
    return bookline

def database_clean_read(book):
    """Take book name as input and output as much data as necessary"""
    answer = database.read_from_database(book)
    answer_array = answer.split("\n")
    heading_line = answer_array[0] #headers of each column in database
    for i in range(1, len(answer_array)):
        if answer_array[i] == "Book not found":
            continue
        else:
            answer_array[i] = check_overdue(answer_array[i])
            heading_line = heading_line + "\n" + answer_array[i]
    return heading_line

#used for testing purposes
#print(database_clean_read("book1"))
