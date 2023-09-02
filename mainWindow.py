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
    add_task = tk.Button(root,text="Add Task",font="Times 15 bold",bg="#273c75",fg="White",width=20,height=2,cursor="hand2",command=addbutton)
    add_task.place(x=50,y=100)

    delete_task = tk.Button(root,text="Delete Task",fg="White",font="Times 15 bold",bg="#273c75",width=20,height=2,cursor="hand2")
    delete_task.place(x=50,y=200)

    exit = tk.Button(root,text="Exit",fg="White",font="Times 15 bold",bg="#273c75",width=20,height=2,cursor="hand2", command=root.destroy)
    exit.place(x=50,y=682.5)

    #add table
    my_tree = ttk.Treeview(root,height=15)
    #define table columns
    my_tree['columns']=("Description","Time","Status")
    #set fonts
    custom_font = ("Times",20)
    my_tree.tag_configure("custom_font",font=custom_font)
    #set styles
    s = ttk.Style()
    s.theme_use('clam')
    s.configure('Treeview.Heading',background="Light Blue",font="Times 20")
    s.configure('Treeview',rowheight=40)
    #format our columns
    my_tree.column("#0",width=100,minwidth=25)
    my_tree.column("Description",anchor=W,width=400)
    my_tree.column("Time",anchor=CENTER,width=200)
    my_tree.column("Status",anchor=CENTER,width=200)
    #create headdings
    my_tree.heading("#0",text="ID",anchor=CENTER)
    my_tree.heading("Description",text="Description",anchor=CENTER)
    my_tree.heading("Time",text="Time",anchor=CENTER)
    my_tree.heading("Status",text="Status",anchor=CENTER)
    #add data
    my_tree.insert(parent='',index='end',iid=0,text='01',values=('1st Period','7.30','No'),tags=("custom_font"))
    my_tree.insert(parent='',index='end',iid=1,text='02',values=('2nd Period','8.10','No'),tags=("custom_font"))
    my_tree.insert(parent='',index='end',iid=2,text='03',values=('3rd Period','8.50','No'),tags=("custom_font"))
    my_tree.insert(parent='',index='end',iid=3,text='04',values=('4th Period','9.30','No'),tags=("custom_font"))
    my_tree.insert(parent='',index='end',iid=4,text='05',values=('5th Period','10.10','No'),tags=("custom_font"))
    my_tree.insert(parent='',index='end',iid=5,text='06',values=('Interval','10.50','No'),tags=("custom_font"))
    my_tree.insert(parent='',index='end',iid=6,text='07',values=('6th Period','11.30','No'),tags=("custom_font"))
    my_tree.insert(parent='',index='end',iid=7,text='08',values=('7th Period','12.10','No'),tags=("custom_font"))
    my_tree.insert(parent='',index='end',iid=8,text='09',values=('8th Period','12.50','No'),tags=("custom_font"))
    
    #pack to the screen
    my_tree.place(x=550,y=100)
    

    root.mainloop()