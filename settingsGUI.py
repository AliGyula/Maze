import tkinter as tk
from tkinter import Label,Entry,Checkbutton,Button

class settings(tk.Frame):
    def __init__(self,master=None):
        self.width=0
        self.height=0
        self.cell=0
        self.speed=0
        self.isLaunching=0
        


        self.widthEntry=None
        self.heightEntry=None
        self.cellEntry=None
        self.speedEntry=None
        self.editorBtn=None

        tk.Frame.__init__(self, master)
        self.var = tk.IntVar()
        self.pack()
        self.createWidgets()
        
    

    def createWidgets(self):
        self.master.title("Settings")
        self.master.geometry("300x210")
        self.master.resizable(False,False)

        widthLabel=Label(self.master,text="width:")
        heightLabel=Label(self.master,text="height:")
        cellLabel=Label(self.master,text="cell size:")
        speedLabel=Label(self.master,text="speed(1-100):")
        

        self.widthEntry=Entry(self.master)
        self.heightEntry=Entry(self.master)
        self.cellEntry=Entry(self.master)
        self.speedEntry=Entry(self.master)
        self.editorBtn=Checkbutton(self.master, text="launch level editor", variable=self.var)

        btn=Button(self.master,text="OK!",command=self.getSettings)

        widthLabel.pack()
        self.widthEntry.pack()
        heightLabel.pack()
        self.heightEntry.pack()
        cellLabel.pack()
        self.cellEntry.pack()
        speedLabel.pack()
        self.speedEntry.pack()
        self.editorBtn.pack()
        btn.pack() 

    def getSettings(self):
            self.width=self.widthEntry.get()
            self.height=self.heightEntry.get()
            self.cell=self.cellEntry.get()
            self.speed=self.speedEntry.get()
            self.isLaunching=self.var.get()
            self.master.destroy()