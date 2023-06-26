import tkinter as tk
from constants import FRM_WIDTH
from tkinter import ttk


class Scrollable(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        canvas= tk.Canvas(self, bg='#4A7A8C', width=FRM_WIDTH, height=20 )
        canvas.frame= ttk.Frame(self.canvas)
        self.horizont_bar= tk.Scrollbar(self, orient='horizontal')
        canvas.frame.rowconfigure(990, weight=1)
        canvas.config(width=FRM_WIDTH,height=10)
        #self.canvas.config(scrollregion= self.canvas.bbox("all"))
        canvas.configure(
            xscrollcommand = self.horizont_bar.set
            )
        self.horizont_bar.config(command= self.canvas.xview)
        canvas.grid(column=0, row=0, columnspan=8, sticky='e')
        canvas.bind('<Configure>', self.update_canvas(canvas))   
        canvas.configure(scrollregion=self.bbox("al"))
        self.window = canvas.create_window((0, 0), window=canvas.frame, anchor=tk.NW)

        self.update_idletasks()
        #self.canvas.configure(xscrollcommand=self.xscroll.set)
    def update_canvas(self,canvas, event):
            # if the new canvas's width (event.width) is larger than the content's 
            # minimum width (content.winfo_reqwidth()) then make canvas.frame the 
            # same width as the canvas
            if event.width > self.winfo_reqwidth():
                canvas.itemconfigure(self.window, width=event.width)
    
    def updateScrollRegion(self,canvas):
        canvas.update_idletasks()
        canvas.config(scrollregion=self.bbox())

 
    '''    self.canvas.bind('<Configure>', self.__fill_canvas)
        self.windows_item = self.canvas.create_window(0,0, window=self)
    def __fill_canvas(self, event):
        "Enlarge the windows item to the canvas width"

        canvas_width = event.width
        self.canvas.itemconfig(self.windows_item, width = canvas_width)
    def update(self):
        "Update the canvas and the scrollregion"

        self.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox(self.windows_item))'''
        #self.horizont_bar.grid(column=0, row=1, sticky='EW')
        
        #self.frm_scrollable = tk.Frame(self.canvas)
        #self.frm_scrollable.bind(
        #    '<Configure>',
        #    lambda event: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        #)
        #self.canvas.create_window((0, 0), window=self.frm_scrollable, anchor='e')'''
        
