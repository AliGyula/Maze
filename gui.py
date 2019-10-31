from tkinter import Canvas
from mazeGenerator import mazeGenerator
import tkinter as tk

class gui(tk.Frame):

    def __init__(self,width,height,title, master=None):
        self.winWidth=width
        self.winHeight=height
        self.expandedWidth=self.winWidth+5
        self.expandedHeight=self.winHeight+6
        self.title=title

        tk.Frame.__init__(self, master)
        self.master.title(self.title)
        if self.title=='Level editor':
            self.winSize=str(self.expandedWidth)+'x'+str(self.expandedHeight+30)
        else:
            self.winSize=str(self.expandedWidth)+'x'+str(self.expandedHeight)
        self.master.geometry(self.winSize)
        self.master.resizable(False, False)
        self.pack()
        self.createCanvas()

    def createCanvas(self):
        self.canvas=Canvas(self.master,width=self.expandedWidth,height=self.expandedHeight,background='floral white')
        self.canvas.pack()