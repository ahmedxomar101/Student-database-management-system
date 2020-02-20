from tkinter import *
import backend
    
    
def get_selected_row(event):
    ''' get_selected_row function to get content of the selected row.
    
        Arguments
        ---------
        event: a virtual interrupt.
    '''
    global selected_tuple
    if lb1.curselection() != ():
 
        index = lb1.curselection()[0]
        selected_tuple = lb1.get(index)
        clear_entries()
        e1.insert(END,selected_tuple[1])
        e2.insert(END,selected_tuple[2])
        e3.insert(END,selected_tuple[3])
        e4.insert(END,selected_tuple[4])

def view_command():
    ''' view_command function to show the output database.
    
    '''
    lb1.delete(0,END)  
    for row in backend.view():
        lb1.insert(END,row)

def search_command():
    ''' search_command function to search in the database.
    
    '''
    lb1.delete(0,END)
    for row in backend.search(fn.get(),ln.get(),term.get(),gpa.get()):
        lb1.insert(END,row)
    clear_entries()

def add_command():
    ''' add_command function to add a new student to the database.
    
    '''
    backend.insert(fn.get(),ln.get(),term.get(),gpa.get())
    clear_entries()
    view_command()

def update_command():
    ''' update_command function to update the data of a specific student.
    
    '''
    backend.update(selected_tuple[0],fn.get(),ln.get(),term.get(),gpa.get())
    clear_entries()
    view_command()
    
def delete_command():
    ''' delete_command function to delete the data of a specific student.
    
    '''
    index = lb1.curselection()[0]
    selected_tuple = lb1.get(index)
    backend.delete(selected_tuple[0])
    clear_entries()
    view_command()

def delete_data_command():
    ''' delete_data_command function to delete the database.
    
    '''
    backend.delete_data()
    view_command()

def clear_entries():
    ''' clear_entries function to clear content of entries.
    
    '''
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    
def clear_command():
    ''' view_command function to clear content of Listbox.
    
    '''
    lb1.delete(0,END)
    clear_entries()
   
wind = Tk()

fn = StringVar()
ln = StringVar()
term = StringVar()
gpa = StringVar()

l0 = Label(wind, text = "Students", width = "10", fg = "blue")
l0.config(font=("Courier", 15))

l00 = Label(wind, text = "Database", width = "10", fg = "blue")
l00.config(font=("Courier", 15))

l1 = Label(wind, text = "First Name", width = "10")
l2 = Label(wind, text = "Last Name", width = "10")
l3 = Label(wind, text = "Term", width = "10")
l4 = Label(wind, text = "GPA", width = "10")

e1 = Entry(wind, textvariable =fn)
e2 = Entry(wind, textvariable =ln)
e3 = Entry(wind, textvariable =term)
e4 = Entry(wind, textvariable =gpa)

b1 = Button(wind, text = "View all", width = "15", command = view_command)
b2 = Button(wind, text = "Search", width = "15", command = search_command)
b3 = Button(wind, text = "Add New", width = "15", command = add_command)
b4 = Button(wind, text = "Update", width = "15", command = update_command)
b5 = Button(wind, text = "Delete", width = "15", command = delete_command)
b6 = Button(wind, text = "Clear", width = "15", command = clear_command)
b7 = Button(wind, text = "Delete all Students", width = "15", command = delete_data_command)
b8 = Button(wind, text = "Exit", width = "15", command = wind.destroy)

lb1 = Listbox(wind, height = 6, width = 35)
lb1.bind('<<ListboxSelect>>',get_selected_row)

sc = Scrollbar(wind)

l0.grid(row=0,column=1)
l00.grid(row=0,column=2)
l1.grid(row=1,column=0)
l2.grid(row=1,column=2)
l3.grid(row=2,column=0)
l4.grid(row=2,column=2)

e1.grid(row=1,column=1)
e2.grid(row=1,column=3)
e3.grid(row=2,column=1)
e4.grid(row=2,column=3)

b1.grid(row=3,column=3)
b2.grid(row=4,column=3)
b3.grid(row=5,column=3)
b4.grid(row=6,column=3)
b5.grid(row=7,column=3)
b6.grid(row=8,column=3)
b7.grid(row=9,column=3)
b8.grid(row=10,column=3)

lb1.grid(row=4, column=0,rowspan=8, columnspan=2)

sc.grid(row=4,column=2,rowspan=8)

lb1.configure(yscrollcommand=sc.set)
sc.configure(command=lb1.yview)

wind.mainloop()
