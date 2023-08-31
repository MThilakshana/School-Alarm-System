import tkinter as tk
class mainWindow:

    #create window
    window = tk.Tk()
    window.title("School Alarm System 1.0")
    #set backgroung color
    window.configure(background = "#353b48")
    #set window size
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window.geometry(f"{screen_width}x{screen_height}")
    
    #add labels
    title = tk.Label(window,text="School Alarm System",fg="White",bg="#353b48",font="Times 35 bold").pack()

    #add buttons
    add_task = tk.Button(window,text="Add Task",font="Times 15 bold",bg="#273c75",fg="White",width=20,height=2,cursor="hand2")
    add_task.place(x=50,y=100)

    delete_task = tk.Button(window,text="Delete Task",fg="White",font="Times 15 bold",bg="#273c75",width=20,height=2,cursor="hand2")
    delete_task.place(x=50,y=200)

    exit = tk.Button(window,text="Exit",fg="White",font="Times 15 bold",bg="#273c75",width=20,height=2,cursor="hand2", command=window.destroy)
    exit.place(x=50,y=500)

    #add table

    window.mainloop()