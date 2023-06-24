import tkinter as tk
from tkinter import ttk
from services.db_repo import get_pyposude, get_pyposude_by_id, update_pyposude, insert_pyposude
from services.data_simulation import simul_data_for_pyposuda, save_sync_data
from functools import partial
from constants import *
from models.posuda import Posuda
class TtkPosude(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.packing = []
        btn_add_pot = ttk.Button(self, text='Dodaj posudu', command= self.add_new_pot)
        btn_add_pot.grid(row= 7, column=2, padx=BODY_PADX, pady= BODY_PADY)
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

        self.pack_forget ()       
        ttk.Label(self, text='Naziv posude').grid(row= 1, column=0, padx=BODY_PADX, pady= BODY_PADY)
        ent_naziv_posude_var= tk.StringVar()
        ent_naziv_posude_var.set(posuda.naziv)
        tk.Entry(self, textvariable= ent_naziv_posude_var, font=BODY_FONT).grid(row= 1, column=1, padx=BODY_PADX, pady= BODY_PADY)

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

        btn_sync = ttk.Button(self, text='SYNC', command= partial(self.sync_senzor_data, posuda_id))
        btn_sync.grid(row= 7, column=1, padx=BODY_PADX, pady= BODY_PADY)
        
    def sync_senzor_data(self, posuda_id):
        vlaga_zemlje, ph_zemlje, temp_zraka, razina_svjetla = simul_data_for_pyposuda()
        save_sync_data(posuda_id, vlaga_zemlje, ph_zemlje, temp_zraka, razina_svjetla)
        update_pyposude(posuda_id, None, vlaga_zemlje, ph_zemlje, temp_zraka, razina_svjetla, None)
        self.open_pot(posuda_id)

    def add_new_pot(self):
        self.pack_forget()
        ttk.Label(self, text='Naziv posude').grid(row= 1, column=0, padx=BODY_PADX, pady= BODY_PADY)
        ent_naziv_posude_var = tk.StringVar()
        tk.Entry(self, textvariable= ent_naziv_posude_var, font=BODY_FONT).grid(row= 1, column=1, padx=BODY_PADX, pady= BODY_PADY)
        ttk.Label(self, text='ID biljke').grid(row= 2, column=0, padx=BODY_PADX, pady= BODY_PADY)
        ent_id_biljke_var = tk.StringVar()
        tk.Entry(self, textvariable= ent_id_biljke_var, font=BODY_FONT).grid(row= 2, column=1, padx=BODY_PADX, pady= BODY_PADY)
        def save_pot():
            posuda = Posuda(ent_naziv_posude_var.get(),None,None,None,None,ent_id_biljke_var.get())
            insert_pyposude(posuda)
        btn_save_pot = ttk.Button(self, text='Spremi', command= save_pot)
        btn_save_pot.grid(row= 3, column=1, padx=BODY_PADX, pady= BODY_PADY)
       
       