"""Use functions from database.py to take data and send it to the menu"""

import database




def get_name_list(book):
    """Get a list of book names"""
    name_list = database.genre_book_name(book)
    return name_list

def get_book_count(book):
    
    """Get a list of total loans of each book of the same genre"""
    book_count = database.logfile_count(book)
    return book_count
