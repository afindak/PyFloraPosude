import tkinter as tk
from tkinter import ttk
from services.db_repo import get_pyposude, get_pyposude_by_id, update_pyposude, insert_pyposude, get_pybiljke_by_id, update_biljka_posude, take_out_plant
from services.data_simulation import simul_data_for_pyposuda, save_sync_data
from functools import partial
from constants import *
from models.posuda import Posuda
from datetime import datetime as dt
from .canvas_scroll import Scrollable

class TtkPosude(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.packing = []
        btn_add_pot = ttk.Button(self, text='Dodaj posudu', command= self.add_new_pot)
        btn_add_pot.grid(row= 9, column= 1, padx= BODY_PADX, pady= BODY_PADY)

    def list_pyposude(self):
        btn_container = Scrollable(self)
        btn_container.grid(column=0, row=0, columnspan=8,  sticky='EW')
        btn_container.horizont_bar.grid(column=0, row=1, columnspan=7, sticky='EW')
        '''tekst = tk.Text(self)
        tekst.grid(column=0, row=0, columnspan=10,  sticky='EW')
        sb = tk.Scrollbar(self, orient= 'horizontal', command=tekst.xview)
        sb.grid(column=0, row=1)
        tekst.configure(xscrollcommand=sb.set)'''

        for i, posude in enumerate(get_pyposude(True)):
            btn_open_pot = ttk.Button(btn_container,text=f'{posude.naziv}', command=partial(self.open_pot, posude.id))
            #btn_container.update()
            btn_open_pot.grid(row= 0, column= f'{i}', padx=BODY_PADX, pady= BODY_PADY, sticky='e')
            self.packing.append(btn_open_pot)
            #tekst.("end", window=button)
            #ttk.Label(image=posude.id_biljke) 
            #self.scrollbar = tk.Scrollbar(self) # height= not permitted here!
            #self.entry3.config(yscrollcommand= self.scrollbar.set)
            #elf.scrollbar.config(command= self.entry3.yview)
            #self.grid()
            #self.scrollbar.grid(column=6, row=5, rowspan=2,  sticky='W')
    def open_pot(self, posuda_id):
        #for l in self.packing:
        #    l.pack_forget()
        posuda = get_pyposude_by_id(posuda_id)

        self.pack_forget ()       
        ttk.Label(self, text='Naziv posude').grid(row= 1, column=0, padx=BODY_PADX, pady= BODY_PADY)
        ent_naziv_posude_var= tk.StringVar()
        ent_naziv_posude_var.set(posuda.naziv)
        tk.Entry(self, textvariable= ent_naziv_posude_var, font=BODY_FONT, width=10).grid(row= 1, column=1, padx=BODY_PADX, pady= BODY_PADY)

        ttk.Label(self, text='Datum azuriranja').grid(row= 2, column=0, padx=BODY_PADX, pady= BODY_PADY)
        ent_dat_azuriranja_var= tk.StringVar()
        ent_dat_azuriranja_var.set(dt.strftime(posuda.vrijeme_azuriranja, "%d.%m.%Y. %H:%M:%S") )
        tk.Entry(self, textvariable= ent_dat_azuriranja_var, font=BODY_FONT, width=10).grid(row= 2, column=1, padx=BODY_PADX, pady= BODY_PADY)

        ttk.Label(self, text='Vlaga zemlje, %').grid(row= 3, column=0, padx=BODY_PADX, pady= BODY_PADY)
        ent_vlaga_zemlje_var= tk.StringVar()
        ent_vlaga_zemlje_var.set(posuda.vlaga_zemlje)
        ent_vlaga_zemlje = tk.Entry(self, textvariable= ent_vlaga_zemlje_var, font=BODY_FONT, width=10)
        ent_vlaga_zemlje.grid(row= 3, column=1, padx=BODY_PADX, pady= BODY_PADY)
        ent_vlaga_zemlje.config(state=tk.DISABLED)

        ttk.Label(self, text='Temperatura zraka, °C').grid(row= 4, column=0, padx=BODY_PADX, pady= BODY_PADY)
        ent_temp_zraka_var= tk.StringVar()
        ent_temp_zraka_var.set(posuda.temp_zraka)
        ent_temp_zraka = tk.Entry(self, textvariable= ent_temp_zraka_var, font=BODY_FONT, width=10)
        ent_temp_zraka.grid(row= 4, column=1, padx=BODY_PADX, pady= BODY_PADY)
        ent_temp_zraka.config(state= tk.DISABLED)

        ttk.Label(self, text='pH zemlje').grid(row= 5, column=0, padx=BODY_PADX, pady= BODY_PADY)
        ent_ph_zemlje_var= tk.StringVar()
        ent_ph_zemlje_var.set(posuda.ph_zemlje)
        ent_ph_zemlje = tk.Entry(self, textvariable= ent_ph_zemlje_var, font=BODY_FONT, width=10)
        ent_ph_zemlje.grid(row= 5, column=1, padx=BODY_PADX, pady= BODY_PADY)
        ent_ph_zemlje.config(state= tk.DISABLED)

        ttk.Label(self, text='Razina svjetla').grid(row= 6, column=0, padx=BODY_PADX, pady= BODY_PADY)
        ent_razina_svjetla_var= tk.StringVar()
        ent_razina_svjetla_var.set(posuda.razina_svjetla)
        ent_razina_svjetla = tk.Entry(self, textvariable= ent_razina_svjetla_var, font=BODY_FONT, width=10)
        ent_razina_svjetla.grid(row= 6, column=1, padx=BODY_PADX, pady= BODY_PADY)
        ent_razina_svjetla.config(state= tk.DISABLED)
        
        ttk.Label(self, text='Biljka').grid(row= 7, column=0, padx=BODY_PADX, pady= BODY_PADY)
        ent_biljka_var= tk.StringVar()
        if posuda.id_biljke is not None:
            naziv_biljke = get_pybiljke_by_id(posuda.id_biljke).naziv
            ent_biljka_var.set(naziv_biljke)
        tk.Entry(self, textvariable= ent_biljka_var, font=BODY_FONT, width=10).grid(row= 7, column=1, padx=BODY_PADX, pady= BODY_PADY)

        btn_sync = ttk.Button(self, text='SYNC', command= partial(self.sync_senzor_data, posuda_id))
        btn_sync.grid(row= 8, column=1, padx=BODY_PADX, pady= BODY_PADY)

        def update_pot(posuda_id):
            nova_biljka = ent_biljka_var.get()
            if nova_biljka is None or nova_biljka == '':
                take_out_plant(posuda_id)
            else:
                update_biljka_posude(posuda_id, ent_naziv_posude_var.get(), ent_biljka_var.get() )
        btn_update_pot = ttk.Button(self, text='Ažuriraj/ Isprazni', command= partial(update_pot, posuda_id))
        btn_update_pot.grid(row= 9, column= 2, padx= BODY_PADX, pady= BODY_PADY)
        
    def sync_senzor_data(self, posuda_id):
        vlaga_zemlje, ph_zemlje, temp_zraka, razina_svjetla = simul_data_for_pyposuda()
        save_sync_data(posuda_id, vlaga_zemlje, ph_zemlje, temp_zraka, razina_svjetla)
        update_pyposude(posuda_id, None, vlaga_zemlje, ph_zemlje, temp_zraka, razina_svjetla, None)
        self.open_pot(posuda_id)

    def add_new_pot(self):
        #self.pack_forget()
        save_window = tk.Toplevel(self)
        ttk.Label(save_window, text='Naziv posude').grid(row= 1, column=0, padx=BODY_PADX, pady= BODY_PADY)
        ent_naziv_posude_var = tk.StringVar()
        tk.Entry(save_window, textvariable= ent_naziv_posude_var, font=BODY_FONT).grid(row= 1, column=1, padx=BODY_PADX, pady= BODY_PADY)
        ttk.Label(save_window, text='ID biljke').grid(row= 2, column=0, padx=BODY_PADX, pady= BODY_PADY)
        ent_id_biljke_var = tk.StringVar()
        tk.Entry(save_window, textvariable= ent_id_biljke_var, font=BODY_FONT).grid(row= 2, column=1, padx=BODY_PADX, pady= BODY_PADY)
        def save_pot():
            posuda = Posuda(ent_naziv_posude_var.get(),None,None,None,None,ent_id_biljke_var.get())
            insert_pyposude(posuda)
        btn_save_pot = ttk.Button(save_window, text='Spremi', command= save_pot)
        btn_save_pot.grid(row= 3, column=1, padx=BODY_PADX, pady= BODY_PADY)
       
    