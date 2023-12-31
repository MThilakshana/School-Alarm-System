import tkinter as tk
import mysql.connector
import calendar
import os
from playsound import playsound
from tkinter import *
from tkinter import ttk
from time import strftime
from datetime import date,time,datetime
from tktimepicker import AnalogPicker, AnalogThemes
from tkinter import messagebox
from plyer import notification

#conncet to the database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)

#create database and table
cursor = mydb.cursor()
cursor.execute("CREATE DATABASE if not exists schoolalarmsystem")
cursor.execute("use schoolalarmsystem")
cursor.execute("Create table if not exists alarm(day varchar(50),id varchar(10),description varchar(100),time varchar(25))")

#functions 
def sendNotification(result):
    notification.notify(
        title = "School Alarm System - 1.0",
        message = str(result).replace("'","").replace("(","").replace(")","").replace(",",""),
        app_name="Task Manager",
        timeout=10
    )

def restartSystem():
    try:
        path = "C:/Users/DELL/Desktop/Python/School Alarm System/mainWindow.py"
        args = ['mainWindow.py']
        os.execv(path, args)
    except Exception as e:
        print("Error during restart:", e)

def playalarm():        
    if(datetime.now().hour > 12 ):
        timeVal = str((datetime.now().hour-12)).lstrip('0') + ":" + str(datetime.now().minute) + ":" + str(datetime.now().second) + " PM"
    else:
        timeVal = str(datetime.now().hour).lstrip('0') + ":" + str(datetime.now().minute) + ":" + str(datetime.now().second) + " AM"

    for item_id in my_tree.get_children():
        item_data = my_tree.item(item_id)
        values = item_data["values"]
        if(values[2] == timeVal):
            
            sql = "SELECT description FROM alarm WHERE time = %s"
            record = values[2]
            cursor.execute(sql,(record,))
            result = cursor.fetchone()
            mydb.commit()
    
            sendNotification(result)
            playsound("C:/Users/DELL/Desktop/Python/School Alarm System/sound.mp3")
            break
    
def exitwindow(root):
    result = messagebox.askyesno("Confirmation", "Do you want to exit?")
    if result:
        root.destroy()
    
def saveData(myday,id,description,selectedTime,top):
    timeVal = f"{selectedTime[0]}:{selectedTime[1]}:0 {selectedTime[2]}"
    #save data in database
    sql = "INSERT INTO alarm VALUES(%s,%s,%s,%s)"
    record = (myday,id,description,timeVal)
    cursor.execute(sql,record)
    mydb.commit()
    #message box    
    message = messagebox.showinfo("Message","Data saved successfully!")
    top.destroy()
    addDataToTable()

def addbutton():
    top = Toplevel()
    top.title('Add New Task - School Alarm System 1.0')
    top.geometry("950x700")
    top.configure(background="#353b48")
    title = tk.Label(top,text="Add New Task",fg="White",bg="#353b48",font="Times 30 bold").pack()
    select_day = tk.Label(top,text="Select Day",fg="White",bg="#353b48",font="Times 15 bold").place(x=40,y=100)
    combo_val = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    day_combobox = ttk.Combobox(top,values=combo_val,width=20,font="Times 15 bold")
    day_combobox.place(x=200,y=100)
    task_id = tk.Label(top,text="ID",fg="White",bg="#353b48",font="Times 15 bold").place(x=40,y=150)
    id_entry = tk.Entry(top,font="Times 15 bold",width=22)
    id_entry.place(x=200,y=150)
    description = tk.Label(top,text="Description",fg="White",bg="#353b48",font="Times 15 bold").place(x=40,y=200)
    description_entry = tk.Entry(top,font="Times 15 bold",width=70)
    description_entry.place(x=200,y=200)
    time_label = tk.Label(top,text="Time",fg="White",bg="#353b48",font="Times 15 bold").place(x=40,y=250)
    
    #set the clock
    time_picker = AnalogPicker(top)
    time_picker.place(x=200,y=250)
    theme = AnalogThemes(time_picker)
    theme.setNavyBlue()
    
    exit = tk.Button(top, text="Exit",font="Times 15 bold",bg="#273c75",fg="White",width=10,height=1,cursor="hand2",command=top.destroy).place(x=800,y=650)
    save = tk.Button(top, text="Save",font="Times 15 bold",bg="#273c75",fg="White",width=10,height=1,cursor="hand2",command=lambda:saveData(day_combobox.get(),id_entry.get(),description_entry.get(),time_picker.time(),top)).place(x=650,y=650)

    top.mainloop()
    
def deleteData(id_entry,top):
    deletequery ="DELETE FROM alarm WHERE id = %s"
    record = id_entry
    cursor.execute(deletequery,(record,))
    mydb.commit()
    messagebox.showinfo("Message","Record Deleted Successfully!")
    top.destroy()
    addDataToTable()
    
def deletebutton():
    
    def searchData():
        try:
            record = "id = " + id_entry.get()
            sql = "SELECT description FROM alarm where id=%s"
            record = id_entry.get()
            cursor.execute(sql, (record,))
            result = cursor.fetchone()
            if result is not None:
                result = str(result).replace("{","").replace("}","").replace("(","").replace(")","").replace("'","").replace(",","")
                description.insert(0, result)
            else:
                messagebox.showinfo("Warning!","Invalid ID, Try Again!")
                top.destroy()
                deletebutton()
        
        except mysql.connector.Error as error:
            messagebox.showinfo("Warning!","Error Found - ",error)       
        
    top = Toplevel()
    top.title('Delete Task - School Alarm System 1.0')
    top.geometry('600x350')
    top.configure(background="#353b48")
    title = tk.Label(top,text="Delete Task",fg="White",bg="#353b48",font="Times 30 bold").pack()
    task_id = tk.Label(top,text="ID",fg="White",bg="#353b48",font="Times 15 bold").place(x=40,y=100)
    id_entry = tk.Entry(top,font="Times 15 bold",width=22)
    id_entry.place(x=200,y=100)
    description_label = tk.Label(top,text="Description",fg="White",bg="#353b48",font="Times 15 bold").place(x=40,y=150)
    description = tk.Entry(top,font="Times 15 bold",width=35)
    description.place(x=200,y=150)
    searchbtn = tk.Button(top,text="Search",font="Times 15 bold",bg="#273c75",fg="White",width=8,height=1,cursor="hand2",command=searchData).place(x=450,y=95)
    deletebtn = tk.Button(top,text="Delete",font="Times 15 bold",bg="#273c75",fg="White",width=10,height=1,cursor="hand2",command=lambda:deleteData(id_entry.get(),top)).place(x=225,y=250)
    cnacelbtn = tk.Button(top,text="Cancel",font="Times 15 bold",bg="#273c75",fg="White",width=10,height=1,cursor="hand2",command=top.destroy).place(x=225,y=300)
    top.mainloop()
    
def updateData(id,description,time,top):
    sql = "UPDATE alarm SET description = %s , time = %s WHERE id = %s"
    record = (description,time,id)
    cursor.execute(sql,record)
    mydb.commit()
    messagebox.showinfo("Message","Data Updated Successfully!")
    top.destroy()
    addDataToTable()
    
def updatebutton():
    
    def searchData():
        try:
            record = "id = " + id_entry.get()
            sql = "SELECT description, time FROM alarm where id=%s"
            record = id_entry.get()
            cursor.execute(sql, (record,))
            result = cursor.fetchone()
            if result is not None:
                des = str(result[0]).replace("{","").replace("}","").replace("(","").replace(")","").replace("'","").replace(",","")
                tim = str(result[1]).replace("{","").replace("}","").replace("(","").replace(")","").replace("'","").replace(",","")
                description.insert(0, des)
                time.insert(0,tim)
            else:
                messagebox.showinfo("Warning!","Invalid ID, Try Again!")
                top.destroy()
                updatebutton()
        
        except mysql.connector.Error as error:
            messagebox.showinfo("Warning!","Error Found - ",error)
    
    top = Toplevel()
    top.title('Update Task - School Alarm System 1.0')
    top.geometry('600x350')
    top.configure(background="#353b48")
    title = tk.Label(top,text="Update Task",fg="White",bg="#353b48",font="Times 30 bold").pack()
    task_id = tk.Label(top,text="ID",fg="White",bg="#353b48",font="Times 15 bold").place(x=40,y=100)
    id_entry = tk.Entry(top,font="Times 15 bold",width=22)
    id_entry.place(x=200,y=100)
    description_label = tk.Label(top,text="Description",fg="White",bg="#353b48",font="Times 15 bold").place(x=40,y=150)
    description = tk.Entry(top,font="Times 15 bold",width=35)
    description.place(x=200,y=150)
    time_label = tk.Label(top,text="Time",fg="White",bg="#353b48",font="Times 15 bold").place(x=40,y=200)
    time = tk.Entry(top,font="Times 15 bold",width=35)
    time.place(x=200,y=200)
    searchbtn = tk.Button(top,text="Search",font="Times 15 bold",bg="#273c75",fg="White",width=8,height=1,cursor="hand2",command=searchData).place(x=450,y=95)
    updatebtn = tk.Button(top,text="Update",font="Times 15 bold",bg="#273c75",fg="White",width=10,height=1,cursor="hand2",command=lambda:updateData(id_entry.get(),description.get(),time.get(),top)).place(x=425,y=275)
    cancelbtn = tk.Button(top,text="Cancel", font="Times 15 bold",width=10,height=1,bg="#273c75",fg="White",command=top.destroy).place(x=40,y=275)
    top.mainloop()  

def time_clock():
    #string1 = strftime('%I:').lstrip('0')
    string2 = strftime('%I:%M:%S %p')
    #string = string1 + string2
    clock.config(text=string2)
    clock.after(100, time_clock)
    playalarm()
    
def addDataToTable():
    my_tree.delete(*my_tree.get_children())
    condition ="day = %s"
    record = (day,)
    mysql = "select id,description,time from alarm where " + condition
    cursor.execute(mysql,record)
    count = 0
    for row in cursor:
        my_tree.insert(parent='',index='end',iid=count,text='',values=row,tags=("custom_font"))
        count = count + 1


#get date and time
today_date = date.today()
day = calendar.day_name[today_date.weekday()]

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
title = tk.Label(root,text="School Alarm System 1.0",fg="White",bg="#353b48",font="Times 35 bold").pack()
time = tk.Label(root,text="Time",font="Times 20 bold",bg="#353b48",fg="White")
time.place(x=1250,y=100)
clock = tk.Label(root,font = "Times 20 bold", bg = "#353b48", fg = "White")
clock.place(x=1250, y= 140)
dateset = tk.Label(root,text="Date",font="Times 20 bold",bg="#353b48",fg="White")
dateset.place(x=550,y=100)
dateplace = tk.Label(root,text=today_date,font = "Times 20 bold", bg = "#353b48", fg = "White")
dateplace.place(x=550,y=140)
dayset = tk.Label(root,text="Day",font="Times 20 bold",bg="#353b48",fg="White")
dayset.place(x=900,y=100)
dayplace = tk.Label(root,text=day,font="Times 20 bold",bg="#353b48",fg="White")
dayplace.place(x=900,y=140)

#add buttons
add_task = tk.Button(root,text="Add Task",font="Times 15 bold",bg="#273c75",fg="White",width=20,height=2,cursor="hand2",command=addbutton)
add_task.place(x=50,y=100)

delete_task = tk.Button(root,text="Delete Task",fg="White",font="Times 15 bold",bg="#273c75",width=20,height=2,cursor="hand2",command=deletebutton)
delete_task.place(x=50,y=200)

update_task = tk.Button(root,text="Update Task",fg="White",font="Times 15 bold",bg="#273c75",width=20,height=2,cursor="hand2",command=updatebutton)
update_task.place(x=50,y=300)

exit = tk.Button(root,text="Exit",fg="White",font="Times 15 bold",bg="#273c75",width=20,height=2,cursor="hand2", command=lambda:exitwindow(root))
exit.place(x=50,y=700)

#add table
my_tree = ttk.Treeview(root,height=13)
#define table columns
my_tree['columns']=("ID","Description","Time")
#set fonts
custom_font = ("Times",20)
my_tree.tag_configure("custom_font",font=custom_font)
#set styles
s = ttk.Style()
s.theme_use('clam')
s.configure('Treeview.Heading',background="Light Blue",font="Times 20")
s.configure('Treeview',rowheight=40)
#format our columns
my_tree.column("#0",width=0,stretch=NO)
my_tree.column("ID",anchor=CENTER,width=250)
my_tree.column("Description",anchor=W,width=400)
my_tree.column("Time",anchor=CENTER,width=250)
#create headdings
my_tree.heading("#0",anchor=CENTER)
my_tree.heading("ID",text="ID",anchor=CENTER)
my_tree.heading("Description",text="Description",anchor=CENTER)
my_tree.heading("Time",text="Time",anchor=CENTER)
#add data


addDataToTable()

#pack to the screen
my_tree.place(x=550,y=200)

#set time
time_clock()
    
playalarm()

root.mainloop()