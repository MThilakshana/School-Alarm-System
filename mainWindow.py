import tkinter as tk
from tkinter import *
from tkinter import ttk
class mainWindow:
    
    #functions


    #create window
    root = tk.Tk()
    root.title("School Alarm System 1.0")
    #set backgroung color
    root.configure(background = "#353b48")
    #set window size
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}")
        
    #add labels
    title = tk.Label(root,text="School Alarm System",fg="White",bg="#353b48",font="Times 35 bold").pack()

    #add buttons
    add_task = tk.Button(root,text="Add Task",font="Times 15 bold",bg="#273c75",fg="White",width=20,height=2,cursor="hand2")
    add_task.place(x=50,y=100)

    delete_task = tk.Button(root,text="Delete Task",fg="White",font="Times 15 bold",bg="#273c75",width=20,height=2,cursor="hand2")
    delete_task.place(x=50,y=200)

    exit = tk.Button(root,text="Exit",fg="White",font="Times 15 bold",bg="#273c75",width=20,height=2,cursor="hand2", command=root.destroy)
    exit.place(x=50,y=500)

    #add table
    my_tree = ttk.Treeview(root)
    #define table columns
    my_tree['columns']=("Description","Time","Status")
    #format our columns
    my_tree.column("#0",width=50,minwidth=25)
    my_tree.column("Description",anchor=W,width=120)
    my_tree.column("Time",anchor=CENTER,width=100)
    my_tree.column("Status",anchor=CENTER,width=100)
    #create headdings
    my_tree.heading("#0",text="ID",anchor=CENTER)
    my_tree.heading("Description",text="Description",anchor=CENTER)
    my_tree.heading("Time",text="Time",anchor=CENTER)
    my_tree.heading("Status",text="Status",anchor=CENTER)
    #add data
    my_tree.insert(parent='',index='end',iid=0,text='01',values=('1st Period','7.30','No'))
    
    #pack to the screen
    my_tree.place(x=550,y=100)
    

    root.mainloop()