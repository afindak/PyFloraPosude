
import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Frame):
    def __init__(self,master)-> None:
        super().__init__(master)

        tab_control = ttk.Notebook(self)

        ttk_posude = ttk.Frame(tab_control)
        ttk_biljke = ttk.Frame(tab_control)
        ttk_moj_profil = ttk.Frame(tab_control)

        tab_control.add(ttk_posude, text = 'Posude')
        tab_control.add(ttk_biljke, text = 'Biljke')
        tab_control.add(ttk_moj_profil, text= 'Moj profil')

        tab_control.pack(expand=1, fill= 'both')

