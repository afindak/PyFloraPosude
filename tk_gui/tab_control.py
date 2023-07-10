
import tkinter as tk
from tkinter import ttk
from .tab_posude import TtkPosude
from .tab_biljke import TtkBiljke
from .tab_moj_profil import TtkMojProfil
from constants import FRM_HEIGHT, FRM_WIDTH

class TabControl(tk.Frame):
    def __init__(self,master)-> None:
        super().__init__(master)

        # create a notebook
        tab_control = ttk.Notebook(self, width= FRM_WIDTH, height=FRM_HEIGHT)
        tab_control.pack(expand=True, pady=5, fill='y')

        #create frames
        tab_posude = TtkPosude(tab_control)
        frm_biljke = TtkBiljke(tab_control)
        frm_moj_profil = TtkMojProfil(tab_control)

        tab_posude.pack(fill='both', expand=True)
        frm_biljke.pack(fill='both', expand=True)
        frm_moj_profil.pack(fill='both',expand=True)

        #add frames to notebook
        tab_control.add(tab_posude, text = 'Posude')
        tab_control.add(frm_biljke, text = 'Biljke')
        tab_control.add(frm_moj_profil, text= 'Moj profil')

        tab_posude.list_pyposude()

        def on_tab_change(event):
            tab = event.widget.tab('current')
            if tab['text'] == 'Biljke':
                for child in frm_biljke.winfo_children():
                    child.destroy()
                frm_biljke.update()
                frm_biljke.list_pybiljke()

        tab_control.bind("<<NotebookTabChanged>>", on_tab_change)

        
        
        

        
        

