"""Act as intermediary between database.py and manu.py by providing a message"""

import database



def return_confirmation(book_id):
    """Based on boolean returned, output a message"""
    status = database.return_book(book_id)
    if status == True:
        return "Book returned successfully"
    elif status == False:
        return "Error: ID does not exist or book is already available"
    

#used for test purposes
#book_id = "2"
#print(return_confirmation(book_id))
