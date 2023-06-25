import tkinter as tk
from constants import FRM_WIDTH

class Scrollable(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.canvas= tk.Canvas( 
                self,
                bg='#4A7A8C',
                width=FRM_WIDTH,
                height=15#,
                #scrollregion=(0,0,FRM_WIDTH,20)
                )

        self.horizont_bar= tk.Scrollbar(
            self,
            orient='horizontal'
            )
        self.canvas.config(width=FRM_WIDTH,height=10)
        #self.canvas.config(scrollregion= self.canvas.bbox("all"))
        self.canvas.configure(
            xscrollcommand = self.horizont_bar.set
            )
        self.horizont_bar.config(command= self.canvas.xview)
        self.canvas.grid(column=0, row=0, columnspan=8, sticky='e')
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
        #self.canvas.create_window((0, 0), window=self.frm_scrollable, anchor='e')
        