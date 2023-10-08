"""Create a menu system with the desired options that can call on other programs to use their functions"""


import database
import booksearch
import bookreturn
import bookrecommend
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt




win = tk.Tk()
win.title("Python Library System by Arjun Parmar")
win.geometry("1000x160")

#this is where all of the frames that are used are created
menu_frame = Frame(win)
booksearch_frame = Frame(win)
bookcheckout_frame = Frame(win)
bookreturn_frame = Frame(win)
bookrecommend_frame = Frame(win)
graph_frame = Frame(win)


#defines dimensions of the frames
for frame in (menu_frame, booksearch_frame, bookcheckout_frame, bookreturn_frame, bookrecommend_frame, graph_frame):
    frame.grid(row=0, rowspan=2, column=0, sticky='news')



def clear_frame():
    """Go through all widgets in frame and delete each of them"""    
    for widgets in frame.winfo_children():
        widgets.destroy()
    

def search_for_book():
    """Return books that match the entrybox"""
    book = entrybox_search.get()        
    search_answer = booksearch.database_clean_read(book)
    answer_label_search.config(text=search_answer)


    
def return_book():
    """Return message based on entrybox input"""
    book_id = entrybox_return.get()
    return_answer = bookreturn.return_confirmation(book_id)
    answer_label_return.config(text=return_answer)
    


def recommend_book():
    """Return a bar chart based on the book entered in the entrybox"""
    book = entrybox_recommend.get()   
    graph_frame.tkraise()
    clear_frame()
    name_list = bookrecommend.get_name_list(book)
    book_count = bookrecommend.get_book_count(book)    
    f = Figure(figsize = (0.5, 1),dpi =75)
    matplotlib.pyplot.xlabel("Total loans")
    ax = f.add_subplot(111)
    width = .5
    x_pos = [i for i in name_list]
    ax.bar(x_pos, book_count, color='green')
    ax.set_ylabel('Total loans')
    ax.set_title('Popularity of books of a similar genre')
    canvas = FigureCanvasTkAgg(f, graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    back_button_graph = Button(graph_frame, text = "Go back", command = lambda: bookrecommend_frame.tkraise()).place(x = 0, y = 0)


#controls the appearance of the buttons    
st = Style()
st.configure('W.TButton', background='#345', foreground='black', height=100, width=100, font=('Arial', 14 ))

#all of the widgets for the booksearch frame    
booksearch_label = Label(booksearch_frame, text = "Enter book title").place(x = 30,y = 0)
entrybox_search_input = tk.StringVar()
entrybox_search = Entry(booksearch_frame,textvariable = entrybox_search_input, width=80)
entrybox_search.place(x = 120, y = 20)
submitbutton_search = Button(booksearch_frame, text = "Submit", command = search_for_book).place(x = 610, y = 20)    
menubutton_search = Button(booksearch_frame, text = "Go back", command = lambda: menu_frame.tkraise()).place(x = 680, y = 20)
answer_label_search = Label(booksearch_frame, text ="")
answer_label_search.place(x = 30,y = 50)    

#all of the widgets for the bookcheckout frame
#2 sets of entryboxes and buttons since this requires you to enter a member id and a book id
bookcheckout_label_member = Label(bookcheckout_frame, text = "Enter member ID").place(x = 30,y = 0)       
submitbutton_checkout_member = Button(bookcheckout_frame, text = "Submit").place(x = 610, y = 20)    
entrybox_checkout_member = Entry(bookcheckout_frame, width=80).place(x = 120, y = 20)
bookcheckout_label_book = Label(bookcheckout_frame, text = "Enter book ID").place(x = 30,y = 50)       
submitbutton_checkout_book = Button(bookcheckout_frame, text = "Submit").place(x = 610, y = 70)    
entrybox_checkout_book = Entry(bookcheckout_frame, width=80).place(x = 120, y = 70)
menubutton_checkout = Button(bookcheckout_frame, text = "Go back", command = lambda: menu_frame.tkraise()).place(x = 680, y = 20)

#all of the widgets for the bookreturn frame    
bookreturn_label = Label(bookreturn_frame, text = "Enter book ID to return").place(x = 30,y = 0)       
entrybox_return_input = tk.StringVar()
entrybox_return = Entry(bookreturn_frame,textvariable = entrybox_return_input, width=80)
entrybox_return.place(x = 120, y = 20)
submitbutton_return = Button(bookreturn_frame, text = "Submit", command = return_book).place(x = 610, y = 20)
menubutton_return = Button(bookreturn_frame, text = "Go back", command = lambda: menu_frame.tkraise()).place(x = 680, y = 20)
answer_label_return = Label(bookreturn_frame, text ="")
answer_label_return.place(x = 30,y = 50)

#all of the widgets for the bookrecommend frame    
bookrecommend_label = Label(bookrecommend_frame, text = "Enter book title to base recommendations on").place(x = 30,y = 0)       
entrybox_recommend_input = tk.StringVar()
entrybox_recommend = Entry(bookrecommend_frame, textvariable = entrybox_recommend_input, width=80)
entrybox_recommend.place(x = 120, y = 20)
submitbutton_recommend = Button(bookrecommend_frame, text = "Submit", command = recommend_book).place(x = 610, y = 20)
menubutton_recommend = Button(bookrecommend_frame, text = "Go back", command = lambda: menu_frame.tkraise()).place(x = 680, y = 20)





#all the buttons displayed in the main menu. each has a command to raise its respective frame to the top of the window
booksearch_button = ttk.Button(menu_frame, text = "Search for books", style='W.TButton',command = lambda: booksearch_frame.tkraise()).pack()
bookcheckout_button = ttk.Button(menu_frame, text = "Checkout books", style='W.TButton',command = lambda:  bookcheckout_frame.tkraise()).pack()
bookreturn_button = ttk.Button(menu_frame, text = "Return books", style='W.TButton',command = lambda: bookreturn_frame.tkraise()).pack()
bookrecommend_button = ttk.Button(menu_frame, text = "Get recommendations", style='W.TButton',command = lambda:  bookrecommend_frame.tkraise()).pack()
quitprogram_button = ttk.Button(menu_frame, text = "Quit", style='W.TButton',command = win.destroy).pack()   




menu_frame.tkraise()

win.mainloop() 






    
