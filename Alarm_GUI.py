from importlib.metadata import entry_points
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os,time,winsound

def createWidgets():

    label1 = Label(root , text = " Enter the time in hh:mm ")
    label1.grid (row = 0 , column= 0 , padx= 5 , pady= 5)

    global entry1
    entry1 = Entry(root , width= 15 )
    entry1.grid(row = 0 , column= 1)

    label2 = Label(root , text = " Enter the message of the alarm : ")
    label2.grid (row = 1 , column= 0 , padx= 5 , pady= 5)

    global entry2
    entry2 = Entry(root , width= 15 )
    entry2.grid(row = 1 , column= 1)

    but = Button ( root , text= "Submit" , width = 10 , command=submit)
    but.grid(row=2, column=1)

    global label3
    label3 = Label(root , text = "")
    label3.grid(row = 3 , column = 0)

def message1():
    
    global entry1 , label3
    Alarmtimelabel = entry1.get()
    label3.config(text = " The alarm is Counting ... ")
    messagebox.showinfo("Alarm clock ", f"The alarm time is :{Alarmtimelabel}")

def submit():

    global entry1,entry2,label3
    Alarmtime = entry1.get()
    message1()
    currenttime=time.strftime("%H:%M")
    alarmMessage = entry2.get()
    print(f"The alarm time is : {Alarmtime}")
    while Alarmtime != currenttime:
        currenttime = time.strftime("%H:%M")
        time.sleep(1)
    if Alarmtime == currenttime:
        print("Playing alarm sound...")
        winsound.PlaySound("*",winsound.SND_ASYNC)
        label3.config(text="Alarm sound playing >>>")
        messagebox.showinfo("Alarm message", f" The message is : {alarmMessage}")


root = tk.Tk()
root.title("Alarm Clock")
root.geometry("400x150")

createWidgets()

root.mainloop()