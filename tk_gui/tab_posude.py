import tkinter as tk
from tkinter import ttk
from services.db_repo import get_pyposude, get_pyposude_by_id
from functools import partial
from constants import *

class TtkPosude(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.packing = []
    def list_pyposude(self):
        for i, posude in enumerate(get_pyposude(True)):
            btn_open_pot = ttk.Button(self,text=f'{posude.naziv}', command=partial(self.open_pot, posude.id))
            btn_open_pot.grid(row= 0, column= f'{i}', padx=BODY_PADX, pady= BODY_PADY, sticky='e')
            self.packing.append(btn_open_pot)
            #ttk.Label(image=posude.id_biljke) 

    def open_pot(self, posuda_id):
        #for l in self.packing:
        #    l.pack_forget()
        posuda = get_pyposude_by_id(posuda_id)

        ttk.Label(self, text='Naziv posude').grid(row= 1, column=0, padx=BODY_PADX, pady= BODY_PADY)
        ttk.Label(self, text=f'{posuda.naziv}').grid(row= 1, column=1, padx=BODY_PADX, pady= BODY_PADY)

        ttk.Label(self, text='Datum azuriranja').grid(row= 2, column=0, padx=BODY_PADX, pady= BODY_PADY)
        ttk.Label(self, text=f'{posuda.vrijeme_azuriranja}').grid(row= 2, column=1, padx=BODY_PADX, pady= BODY_PADY)

        ttk.Label(self, text='Vlaga zemlje').grid(row= 3, column=0, padx=BODY_PADX, pady= BODY_PADY)
        ttk.Label(self, text=f'{posuda.vlaga_zemlje}').grid(row= 3, column=1, padx=BODY_PADX, pady= BODY_PADY)

        ttk.Label(self, text='Temperatura zraka').grid(row= 4, column=0, padx=BODY_PADX, pady= BODY_PADY)
        ttk.Label(self, text=f'{posuda.temp_zraka}').grid(row= 4, column=1, padx=BODY_PADX, pady= BODY_PADY)

        ttk.Label(self, text='pH zemlje').grid(row= 5, column=0, padx=BODY_PADX, pady= BODY_PADY)
        ttk.Label(self, text=f'{posuda.ph_zemlje}').grid(row= 5, column=1, padx=BODY_PADX, pady= BODY_PADY)

        ttk.Label(self, text='Razina svjetla').grid(row= 6, column=0, padx=BODY_PADX, pady= BODY_PADY)
        ttk.Label(self, text=f'{posuda.razina_svjetla}').grid(row= 6, column=1, padx=BODY_PADX, pady= BODY_PADY)


