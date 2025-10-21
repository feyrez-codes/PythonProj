###############################
# Python GUI Project
#
# Notes:

# If you are here from Github, Hello! 
# Take a look at my ReadMe for details on the project. 

# As of 10/16/25, this project is not functional. Please check back soon as I am working on this every day!

###############################
#Primary GUI superset
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

app = Tk()

app.title("My First Tinkter application!")

main_container = ttk.Frame(app, padding=(3,3,12,12))
main_container.grid(column=0, row=0, sticky=(N,E,S,W))


monster_name = StringVar()
monster_name_entry = ttk.Entry(main_container, width=4, textvariable=monster_name)
monster_name_entry.grid(column=2, row=1, sticky=(N,W))
monster_info = ttk.Label(app, text='Name your custom monster!')
monster_info.grid(column=2, row=1, sticky=(N,W))

app.mainloop()