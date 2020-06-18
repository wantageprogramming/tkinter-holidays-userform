import tkinter as tk
from tkinter import ttk
import pandas as pd

holidays = pd.read_csv('holidays.csv', encoding='latin1')

root = tk.Tk()

canvas = tk.Canvas(root, height=600, width=500)
canvas.pack()

frame = tk.Frame(canvas, bg="green")
frame.place(relwidth=1, relheight=1)

features = [{'wtype': 'entry','bg':'white','width':0.4,'x':0.05, 'y':0.25, 'datacol':'D'},
            {'wtype': 'entry','bg':'white','width':0.9,'x':0.05, 'y':0.35, 'datacol':'E'},
            {'wtype': 'entry','bg':'white','width':0.9,'x':0.05, 'y':0.45, 'datacol':'F'},
            {'wtype': 'entry','bg':'white','width':0.9,'x':0.05, 'y':0.55, 'datacol':'G'},
            {'wtype': 'entry','bg':'white','width':0.3,'x':0.05, 'y':0.65, 'datacol':'H'},
            {'wtype': 'entry','bg':'white','width':0.3,'x':0.45, 'y':0.65, 'datacol':'I'},
            {'wtype': 'entry','bg':'white','width':0.7,'x':0.05, 'y':0.75, 'datacol':'J'},
            {'wtype': 'entry','bg':'white','width':0.7,'x':0.05, 'y':0.85, 'datacol':'K'},
            {'wtype': 'label','bg':'green','width':0.25,'x':0.05, 'y':0.21, 'text':'Holiday ID' },
            {'wtype': 'label','bg':'green','width':0.25,'x':0.05, 'y':0.31, 'text':'Title' },
            {'wtype': 'label','bg':'green','width':0.25,'x':0.05, 'y':0.41, 'text':'URL' },
            {'wtype': 'label','bg':'green','width':0.25,'x':0.05, 'y':0.51, 'text':'Notes' },
            {'wtype': 'label','bg':'green','width':0.30,'x':0.05, 'y':0.61, 'text':'2020' },
            {'wtype': 'label','bg':'green','width':0.30,'x':0.45, 'y':0.61, 'text':'2021' },
            {'wtype': 'label','bg':'green','width':0.25,'x':0.05, 'y':0.71, 'text':'Categories' },
            {'wtype': 'label','bg':'green','width':0.25,'x':0.05, 'y':0.81, 'text':'Regions' }
            ]

class CreateFeatures:
    def __init__(self, frame):
        self.frame = frame
        self.holnumber = 0
        
    def create(self, features, holidaylist):
        self.features = features
        self.holidaylist = holidaylist
        # create entrydata dictionary to store all entry boxes with text variables 
        self.entrydata = {}
        for i in self.features:
            if i['wtype'] == 'entry':
                # entrylist[0] is textvariable, entrylist[1] is entry object
                entrylist = []
                entrylist.append(tk.StringVar())
                x = tk.Entry(self.frame, bg=i['bg'], textvariable=entrylist[0])
                entrylist.append(x)
                # add entry box details to entrydata dictionary
                self.entrydata[i['datacol']] = entrylist
            if i['wtype'] == 'label':
                x = tk.Label(self.frame, bg=i['bg'], text=i['text'], fg="white", anchor="sw")
            x.place(relwidth=i['width'],relx=i['x'],rely=i['y'])
        self.create_buttons()
        self.add_data()
            
    def create_buttons(self):
        self.buttonYears = tk.Button(self.frame, text="Edit Years", bg="yellow", command=self.editYears)
        self.previous_button = tk.Button(self.frame, text="<", bg="yellow", command=self.previous_record)
        self.next_button = tk.Button(self.frame, text=">", bg="yellow", command=self.next_record)
        self.save_button = tk.Button(self.frame, text="Save Changes", bg="yellow", command=self.save_changes)
        self.buttonYears.place(relwidth=0.15, relx=0.80, rely=0.64)
        self.previous_button.place(relwidth=0.10, relx=0.05, rely=0.92)
        self.next_button.place(relwidth=0.10, relx=0.20, rely=0.92)
        self.save_button.place(relwidth=0.20, relx=0.35, rely=0.92)
        
    # opens new window to edit months.
    def editYears(self):
        newwin = tk.Toplevel(self.frame)
        # get data from 'H' in entrydata dictionary, first item in list
        yr2020 = self.entrydata['H'][0].get()
        yr2021 = self.entrydata['I'][0].get()
        newwin.title("Edit Years")
        newwin.geometry("200x100") 
        newwin.resizable(0, 0)
        # create test button
        self.testbutton = tk.Button(newwin, text="edit", bg="yellow", command=self.test)
        self.testbutton.pack()
        
    def test(self):
        self.entrydata['H'][0].set('Hello')
        
    def save_changes(self):
        pass
        
    # add data from csv file to entry boxes
    def add_data(self):
        # loop through entrydata dictionary
        for x, y in self.entrydata.items():
            y[1].delete(0, tk.END)
            
            # eg holidaylist.loc[0, 'D']
            item = self.holidaylist.loc[self.holnumber, x.title()]
            
            # remove NAN from entry boxes and replace with blank
            if item != item:
                item = ""
            y[1].insert(0, item)
            
    #need to check if first or last record
    def next_record(self):
        self.holnumber += 1
        self.add_data()
    
    def previous_record(self):
        self.holnumber -= 1
        self.add_data()
 

newview = CreateFeatures(frame)
newview.create(features, holidays)

tk.mainloop()

