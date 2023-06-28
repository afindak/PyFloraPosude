import tkinter as tk
from constants import *

class Scrollable(tk.Frame):
    def __init__(self, master, background='#333333'):
        super().__init__(master, background=background)

        self.canvas = tk.Canvas(self)
        self.canvas.pack(side='left', fill='both', expand=True)
        self.frm_scrollable = tk.Frame(self.canvas)

        self.scrollbar = tk.Scrollbar(self,
                                orient='vertical',
                                command=self.canvas.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.frm_scrollable.bind(
            '<Configure>',
            lambda event: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.frm_scrollable, anchor='nw')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

class Scrollable_horizontal(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.container = tk.Canvas(self, bg='#4A7A8C', width=FRM_WIDTH, height=25 )
        horizont_bar = tk.Scrollbar(self, orient='horizontal')
 
        self.container.grid(column=0, row=0, columnspan=8,  sticky='EW')
        horizont_bar.grid(row=2, column=0, sticky=tk.EW)
        
        self.frm_container = tk.Frame(self.container, width=FRM_WIDTH, height=25)
        self.frm_container.grid(sticky= tk.NSEW, row= 0, column= 0, columnspan=8)

        self.window = self.container.create_window((0, 0), window= self.frm_container, anchor=tk.NW)

        self.update_idletasks()
        self.container.bind('<Configure>', self.update_canvas)

        self.container.configure(scrollregion=self.frm_container.bbox(tk.ALL))
        self.container.configure(xscrollcommand= horizont_bar.set)
        horizont_bar.configure(command= self.container.xview)
    def update_canvas(self, event):
            # if the new canvas's width (event.width) is larger than the content's 
            # minimum width (content.winfo_reqwidth()) then make canvas.frame the 
            # same width as the canvas
        if event.width > self.frm_container.winfo_reqwidth():
            self.container.itemconfigure(self.window, width=event.width)