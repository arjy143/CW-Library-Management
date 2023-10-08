"""Create functions used to interact with database and logfile and send the relevant data to the menu via booksearch.py, bookcheckout.py, bookreturn.py and bookrecommend.py"""

from datetime import datetime


#functions used for booksearch

def read_from_database(book):
    """Read from database and take all lines of data related to the inputted book name"""
    database = open("database.txt","r")
    flag = 0
    heading_line = database.readline()
    for line in database:  
        if book in line:
            s=line.strip()
            strings=s.split(",")
            strings[2]=strings[2].strip()
            if strings[2]==book:
                flag = 1
                heading_line = heading_line + line
    database.close()             
    if flag == 0: 
        return ('Book not found')
    else:
        return heading_line    
    


def test_data_read():
    """Test whether data is correctly returned"""
    book = input("enter book to search")
    print(read_from_database(book))


def return_last_checkout_date(ID):
    """Open logfile and take the latest checkout date based on the book ID"""
    logfile = open("logfile.txt", "r")
    for line in logfile:
        line = line.strip()
        line_array = line.split(",")
        if line_array[0].strip() == ID and line_array[4].strip() == "0":
            return line_array[3].strip()
    else:
        return False

#functions used for bookreturn
    
def return_book(ID):
    """Open database and if conditions are met, change loan status to '0'. Also alter logfile loan status"""
    exists = False
    database = open("database.txt","r")
    all_lines = database.readlines()
    database.close()
    temp_list=[]
    for i in all_lines:
        line = i.split(",")    
        if line[0].strip() == ID and line[5].strip() != "0":
            line[5] = "0\n"
            exists = True
        for j in range(len(line)):
            if j == 5:
                temp_list.append(line[j])
            else:
                temp_list.append(line[j] + ",")
    temp_string = "" #i used a temporary list to append data and then converted to string to write to file
    for i in temp_list:
        temp_string = temp_string + i
    database = open("database.txt","w") #here it removes all text from the file and rewrites everything including the new line
    database.write(temp_string)
    database.close()
    logfile_alter(exists, ID)
    return exists

    
def logfile_alter(exists, ID):
    """Open logfile and change date from '0' to the current date"""
    if exists == True:
        logfile = open("logfile.txt","r")
        all_lines = logfile.readlines()
        logfile.close()
        temp_list=[]
        for i in all_lines:
            line = i.split(",")
            if line[0].strip() == ID and line[4].strip() == "0":
                line[4] = str(datetime.today().strftime('%d-%m-%y')+"\n")#todays date in correct format         
            for j in range(len(line)):
                if j == 4:
                    temp_list.append(line[j])
                else:
                    temp_list.append(line[j] + ",")
        temp_string = ""
        for i in temp_list:
            temp_string = temp_string + i
        logfile = open("logfile.txt","w") #removes all previous text and rewrites the new data   
        logfile.write(temp_string)
        logfile.close()
    else:
        pass


#functions used for bookrecommend
def get_genre(book):
    """Given a book name, return its genre"""
    database = open("database.txt","r")
    all_lines = database.readlines()
    database.close()
    for i in all_lines:
        line = i.split(",")
        if line[2].strip() == book:
            genre = line[1].strip()
    return genre

def genre_book_id(book):
    """Return a list of book IDs that are of the same genre as the input book"""
    genre = get_genre(book)
    database = open("database.txt","r")
    all_lines = database.readlines()
    database.close()
    id_list=[]
    for i in all_lines:
        line = i.split(",")            
        if line[1].strip() == genre:
            id_list.append(line[0].strip())
    return id_list

def genre_book_name(book):
    """Return a list of book names of the same genre as the input book"""
    genre = get_genre(book)
    database = open("database.txt","r")
    all_lines = database.readlines()
    database.close()
    name_list=[]
    for i in all_lines:
        line = i.split(",")            
        if line[1].strip() == genre:
                name_list.append(line[2].strip())
    return name_list

def logfile_count(book):
    """Return the a list of the total loans of each book of the desired genre"""
    id_list = genre_book_id(book) #gets list of book ids of the same genre
    logfile = open("logfile.txt","r")
    book_count = []
    all_lines = logfile.readlines()
    logfile.close()
    book_count= []
    for i in id_list:
        book_count.append(count_i(i, all_lines))    
    return book_count

def count_i(i, l):
    """Sum the occurences of variable i in the string l"""
    count = 0
    for line in l:
        if line[0] == i:
            count += 1
    return count


                
         

        
