
import tkinter as tk
from tkinter import ttk
from .tab_posude import TtkPosude

class MainWindow(tk.Frame):
    def __init__(self,master)-> None:
        super().__init__(master)

        # create a notebook
        tab_control = ttk.Notebook(self)
        tab_control.pack(expand=True, pady=5, fill='y')

        #create frames
        tab_posude = TtkPosude(tab_control)
        frm_biljke = ttk.Frame(tab_control, width= 650, height=300)
        frm_moj_profil = ttk.Frame(tab_control, width= 650, height=300)

        tab_posude.pack(fill='both', expand=True)
        frm_biljke.pack(fill='both', expand=True)
        frm_moj_profil.pack(fill='both',expand=True)

        #add frames to notebook
        tab_control.add(tab_posude, text = 'Posude')
        tab_control.add(frm_biljke, text = 'Biljke')
        tab_control.add(frm_moj_profil, text= 'Moj profil')

        tab_posude.list_pyposude()

        
        
        

        
        

