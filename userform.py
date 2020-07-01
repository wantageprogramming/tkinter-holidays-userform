import tkinter as tk
from tkinter import ttk
import pandas as pd

holidays = pd.read_csv('holidays.csv', encoding='latin1')

class Mainframe(tk.Tk):
    def __init__(self, widgets, holdata):
        tk.Tk.__init__(self)
        self.widgets = widgets
        self.holdata = holdata
        self.holnumber = 0
        self.entrydata = {}
        self.frame = FirstFrame(self)
        self.frame.pack()

    def change(self, frame):
        for widget in self.winfo_children():
            widget.destroy()
        self.frame = frame(self)
        self.frame.pack() # make new frame

class FirstFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Main application") #master refers to frame
        master.geometry("500x600")
        master['background'] = "yellow"
        #print(self.master.widgets[0]['wtype'])
        
        #loop through widgets, and place them on the frame
        for i in self.master.widgets:
            if i['wtype'] == 'entry':
                # create an entrylist for each entry widget, to be added to data dictionary
                # I don't think I need to store both the text variable and the widget???
                entrylist = []
                entrylist.append(tk.StringVar())
                x = tk.Entry(master, bg=i['bg'], textvariable=entrylist[0])
                entrylist.append(x)
                # add details of all entry boxes to entrydata dictionary
                self.master.entrydata[i['datacol']] = entrylist
            if i['wtype'] == 'label':
                x = tk.Label(master, bg=i['bg'], text=i['text'], fg="white", anchor="sw")
            x.place(relwidth=i['width'],relx=i['x'],rely=i['y'])
        
        self.add_data()
        
        # place buttons
        self.buttonYears = tk.Button(master, text="Edit Years", bg="white", command=self.editYear)
        self.previous_button = tk.Button(master, text="<", bg="white", command=self.previous)
        self.next_button = tk.Button(master, text=">", bg="white", command=self.next)
        self.save_button = tk.Button(master, text="Save Changes", bg="white", command=self.save)
        self.buttonYears.place(relwidth=0.15, relx=0.80, rely=0.64)
        self.previous_button.place(relwidth=0.10, relx=0.05, rely=0.92)
        self.next_button.place(relwidth=0.10, relx=0.20, rely=0.92)
        self.save_button.place(relwidth=0.20, relx=0.35, rely=0.92)
        
    def editYear(self, event=None):
        self.master.change(SecondFrame)
        
    def save(self):
        pass
        
    # add data from csv file to the entry boxes stored in entrydata dictionary
    def add_data(self):
        for x, y in self.master.entrydata.items():
            print(x, y[0])
            item = self.master.holdata.loc[self.master.holnumber, x[0]]
            y[0].set(item)
            
    #need to check if first or last record
    def next(self):
        self.master.holnumber += 1
        self.add_data()
    
    def previous(self):
        self.master.holnumber -= 1
        self.add_data()

class SecondFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        # get year from entrydata dictionary
        year = self.master.entrydata['H'][0].get()
        # create lists to store checkbox variables
        self.yr2020 = []
        self.yr2021 = []
        # set parameters for second frame
        master.title('Edit Years')
        master.geometry("500x600")
        self.create_buttons(year)
        
        btn = tk.Button(master, text="Go", command=self.check1)
        btn.place(relwidth=0.20, relx=0.80, rely=0.64)
        
        # check if I can access data from checkboxes
        self.get_data()
        
    def create_buttons(self, year):
        months = "JFMAMJJASOND"
        for i in range(12):
            self.yr2020.insert(i, tk.IntVar())
            x = tk.Checkbutton(self.master, text=months[i:i+1], bg="yellow", variable=self.yr2020[i])
            x.place(relx=0.20, rely=(i/16) + 0.05)
            if year[i:i+1] == "T":
                x.select()
                
    # check if I can access data from checkboxes
    def get_data(self):
        print(self.yr2020[3].get())
        
    def check1(self):
        self.master.change(FirstFrame)
        
        
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

if __name__=="__main__":
    app=Mainframe(features, holidays)
    app.mainloop()
