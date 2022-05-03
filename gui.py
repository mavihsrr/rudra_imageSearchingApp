from scapper import get_images
from helper import download_images
from tkinter import *
root=Tk()
root.title("Search images")

# setting the windows size
root.geometry("600x400")

# declaring string variable
# for storing name and password
search_query_var=StringVar()
numbers_var=StringVar()

# defining a function that will
# get the name and password and
# print them on the screen
def submit():
    search_query=search_query_var.get()
    numbers=numbers_var.get()     
    print("The search query is : " + search_query)
    print("The input number is : " + numbers)
    search_query_var.set("")
    numbers_var.set("")

def download_it():
    urls=get_images(query="apples")
    if len(urls) !=0:
        download_images(urls)

# search query label
search_query_label = Label(root, text = 'Search query', font=('calibre',10, 'bold'))
# search query inputbox
search_query_entry = Entry(root,textvariable = search_query_var, font=('calibre',10,'normal'))
# number label 
numbers_label = Label(root, text = 'Numbers (max 20)', font = ('calibre',10,'bold'))
# number inputbox
numbers_entry=Entry(root, textvariable = numbers_var, font = ('calibre',10,'normal'))

# buttons
sub_btn=Button(root,text = 'Submit', command = submit)
download_btn=Button(root,text="Download",command=download_it)

search_query_label.grid(row=0,column=0)
search_query_entry.grid(row=0,column=1)
numbers_label.grid(row=1,column=0)
numbers_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)



root.mainloop()



