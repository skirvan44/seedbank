#!/usr/bin/python3
import sqlite3
from os import path
import tkinter as tk
import time

class GardenDB:

    def __init__(self, db_file):
        self.db_file = db_file
        self.db = None

    def first_time(self):
        self.db.execute('''CREATE TABLE journal
                                 (date text,
                                  time text,
                                  weather text,
                                  notes text)''')

        self.db.execute('''CREATE TABLE plants
                                 (common_name text,
                                  latin_name text)''')

        self.db.execute('''CREATE TABLE seed_notes
                                 (common_name text,
                                  company text,
                                  date text,
                                  quantity text)''')

        self.db.execute('''CREATE TABLE plant_notes
                                 (common_name text,
                                  days_to_germinate int,
                                  bugs text,
                                  general_note text''')

    def add_journal_note(date,  notes):
        c.execute("INSERT INTO journal (date, notes) VALUES (date, notes)")

    def add_weather(date,  time, weather):
        c.execute("INSERT INTO journal (date, notes) VALUES (date, notes)")
        
        
    def setup(self):
        first_time = False
        if not path.exists(self.db_file):
            first_time = True
        self.db = sqlite3.connect(self.db_file)
        if first_time:
            self.first_time()
            
    def teardown(self):
        self.db.close()

class GardenGui:

    def __init__(self):
        self.window = tk.Tk()
        self.frame = tk.Frame()

        self.menubar = tk.Menu(self.window)
        file_menu = tk.Menu(self.menubar, tearoff=0)
        new_menu = tk.Menu(file_menu,  tearoff=0)        
        file_menu.add_cascade(label="New", menu=new_menu)
        file_menu.add_command(label="Save", command=self.entry_type_changed)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.window.quit)
        self.menubar.add_cascade(label="File", menu=file_menu)

        new_menu.add_command(label="Plant", command=self.entry_type_changed)
        new_menu.add_command(label="Weather Observation", command=self.entry_type_changed)
        new_menu.add_command(label="Seed Note", command=self.entry_type_changed)
        new_menu.add_command(label="Bug Note", command=self.entry_type_changed)
        new_menu.add_command(label="Germination Note", command=self.entry_type_changed)
        new_menu.add_command(label="General Note", command=self.entry_type_changed)                  
        
        self.window.config(menu=self.menubar)
        
        # New entry type
        self.entry_type = tk.StringVar()
        self.weather_selected = tk.Radiobutton(master=self.frame, text="Weather",
                                            variable=self.entry_type, value = "weather",
                                            command=self.entry_type_changed)
        self.weather_selected.pack(side=tk.LEFT)
        self.journal_note_selected = tk.Radiobutton(master=self.frame, text="Note",
                                            variable=self.entry_type, value = "note",
                                            command=self.entry_type_changed)
        self.journal_note_selected.pack(side=tk.LEFT)


        self.frame.pack()
        self.window.mainloop()        

    def entry_type_changed(self):
        print("Entry type changed!!!!")
                                            
def main():
    gdb = GardenDB("garden.db")
    gdb.setup()

    gg = GardenGui()
    #gg.start()

    
    gdb.teardown()

    

if __name__ == "__main__":
    main()
