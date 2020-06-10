import tkinter as tk
from tkinter import ttk
import pandas as pd

holidays = pd.read_csv('holidays.csv', encoding='latin1')

root = tk.Tk()

canvas = tk.Canvas(root, height=600, width=500)
canvas.pack()

frame = tk.Frame(canvas, bg="green")
frame.place(relwidth=1, relheight=1)

features = [{'wtype': 'entry','bg':'white','width':0.9,'x':0.05, 'y':0.25, 'datacol':'D'},
            {'wtype': 'entry','bg':'white','width':0.9,'x':0.05, 'y':0.35, 'datacol':'E'},
            {'wtype': 'entry','bg':'white','width':0.9,'x':0.05, 'y':0.45, 'datacol':'F'},
            {'wtype': 'entry','bg':'white','width':0.9,'x':0.05, 'y':0.55, 'datacol':'G'},
            {'wtype': 'entry','bg':'white','width':0.2,'x':0.05, 'y':0.65, 'datacol':'H'},
            {'wtype': 'entry','bg':'white','width':0.2,'x':0.50, 'y':0.65, 'datacol':'I'},
            {'wtype': 'entry','bg':'white','width':0.7,'x':0.05, 'y':0.75, 'datacol':'J'},
            {'wtype': 'entry','bg':'white','width':0.7,'x':0.05, 'y':0.85, 'datacol':'K'},
            {'wtype': 'label','bg':'green','width':0.25,'x':0.05, 'y':0.21, 'text':'Holiday ID' },
            {'wtype': 'label','bg':'green','width':0.25,'x':0.05, 'y':0.31, 'text':'Title' },
            {'wtype': 'label','bg':'green','width':0.25,'x':0.05, 'y':0.41, 'text':'URL' },
            {'wtype': 'label','bg':'green','width':0.25,'x':0.05, 'y':0.51, 'text':'Notes' },
            {'wtype': 'label','bg':'green','width':0.25,'x':0.05, 'y':0.61, 'text':'2020' },
            {'wtype': 'label','bg':'green','width':0.25,'x':0.50, 'y':0.61, 'text':'2021' },
            {'wtype': 'label','bg':'green','width':0.25,'x':0.05, 'y':0.71, 'text':'Categories' },
            {'wtype': 'label','bg':'green','width':0.25,'x':0.05, 'y':0.81, 'text':'Regions' }
            ]

class CreateFeatures:
    def __init__(self, frame):
        self.frame = frame
        # will store all the entry boxes in self.widgets
        self.widgets = []
        self.holnumber = 0
        
    def create(self, features, holidaylist):
        self.features = features
        self.holidaylist = holidaylist
        self.datacols = []
        for i in self.features:
            if i['wtype'] == 'entry':
                # this is very messy, need to improve!
                if i['datacol'] == 'H':
                    self.qy2020 = tk.StringVar()
                    x = tk.Entry(self.frame, bg=i['bg'], textvariable=self.qy2020)
                else:
                    x = tk.Entry(self.frame, bg=i['bg'])
                self.datacols.append(i['datacol'])
                self.widgets.append(x)
            if i['wtype'] == 'label':
                x = tk.Label(self.frame, bg=i['bg'], text=i['text'], fg="white", anchor="sw")
            x.place(relwidth=i['width'],relx=i['x'],rely=i['y'])
        self.create_buttons()
        self.add_data()
            
    def create_buttons(self):
        self.button2020 = tk.Button(self.frame, text="edit", bg="yellow", command=self.edit2020)
        self.button2021 = tk.Button(self.frame, text="edit", bg="yellow", command=self.edit2021)
        self.previous_button = tk.Button(self.frame, text="<", bg="yellow", command=self.previous_record)
        self.next_button = tk.Button(self.frame, text=">", bg="yellow", command=self.next_record)
        self.button2020.place(relwidth=0.10, relx=0.26, rely=0.64)
        self.button2021.place(relwidth=0.10, relx=0.74, rely=0.64)
        self.previous_button.place(relwidth=0.10, relx=0.05, rely=0.92)
        self.next_button.place(relwidth=0.10, relx=0.20, rely=0.92)
        
    def edit2020(self):
        newwin = tk.Toplevel(self.frame)
        newwin.title('New Window')
        newwin.geometry("200x100") 
        newwin.resizable(0, 0)
    
    def edit2021(self):
        pass
        
    # add data from csv file to entry boxes
    def add_data(self):
        self.count = 0
        for y in self.widgets:
            y.delete(0, tk.END)
            
            # eg holidaylist.loc[0, 'D']
            item = self.holidaylist.loc[self.holnumber,self.datacols[self.count]]
            
            # remove NAN from entry boxes and replace with blank
            if item != item:
                item = ""
            y.insert(0, item)
            self.count += 1
            
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

