import tkinter as tk
from tkinter import ttk
from functools import partial
from constants import BODY_FONT, BODY_PADX, BODY_PADY
from datetime import datetime as dt
from services.db_repo import get_pybiljke_by_id, update_biljka_posude, take_out_plant, get_pyposude_by_id
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pandas as pd

class OpenPot(tk.Frame):
    def __init__(self, master, posuda_id):
        super().__init__(master)

        posuda = get_pyposude_by_id(posuda_id)
         
        ttk.Label(self, text='Naziv posude').grid(row= 1, column=0, padx=BODY_PADX, pady= BODY_PADY, sticky=tk.W)
        ent_naziv_posude_var= tk.StringVar()
        ent_naziv_posude_var.set(posuda.naziv)
        tk.Entry(self, textvariable= ent_naziv_posude_var, font=BODY_FONT, width=10).grid(row= 1, column=1, padx=BODY_PADX, pady= BODY_PADY)

        ttk.Label(self, text='Datum azuriranja').grid(row= 2, column=0, padx=BODY_PADX, pady= BODY_PADY, sticky=tk.W)
        ent_dat_azuriranja_var= tk.StringVar()
        ent_dat_azuriranja_var.set(dt.strftime(posuda.vrijeme_azuriranja, "%d.%m.%Y. %H:%M:%S") )
        tk.Entry(self, textvariable= ent_dat_azuriranja_var, font=BODY_FONT, width=15).grid(row= 2, column=1, padx=BODY_PADX, pady= BODY_PADY)

        ttk.Label(self, text='Vlaga zemlje, %').grid(row= 3, column=0, padx=BODY_PADX, pady= BODY_PADY, sticky=tk.W)
        ent_vlaga_zemlje_var= tk.StringVar()
        ent_vlaga_zemlje_var.set(posuda.vlaga_zemlje)
        ent_vlaga_zemlje = tk.Entry(self, textvariable= ent_vlaga_zemlje_var, font=BODY_FONT, width=10)
        ent_vlaga_zemlje.grid(row= 3, column=1, padx=BODY_PADX, pady= BODY_PADY)
        ent_vlaga_zemlje.config(state=tk.DISABLED)

        ttk.Label(self, text='Temperatura zraka, °C').grid(row= 4, column=0, padx=BODY_PADX, pady= BODY_PADY, sticky=tk.W)
        ent_temp_zraka_var= tk.StringVar()
        ent_temp_zraka_var.set(posuda.temp_zraka)
        ent_temp_zraka = tk.Entry(self, textvariable= ent_temp_zraka_var, font=BODY_FONT, width=10)
        ent_temp_zraka.grid(row= 4, column=1, padx=BODY_PADX, pady= BODY_PADY)
        ent_temp_zraka.config(state= tk.DISABLED)

        ttk.Label(self, text='pH zemlje').grid(row= 5, column=0, padx=BODY_PADX, pady= BODY_PADY, sticky=tk.W)
        ent_ph_zemlje_var= tk.StringVar()
        ent_ph_zemlje_var.set(posuda.ph_zemlje)
        ent_ph_zemlje = tk.Entry(self, textvariable= ent_ph_zemlje_var, font=BODY_FONT, width=10)
        ent_ph_zemlje.grid(row= 5, column=1, padx=BODY_PADX, pady= BODY_PADY)
        ent_ph_zemlje.config(state= tk.DISABLED)

        ttk.Label(self, text='Razina svjetla').grid(row= 6, column=0, padx=BODY_PADX, pady= BODY_PADY, sticky=tk.W)
        ent_razina_svjetla_var= tk.StringVar()
        ent_razina_svjetla_var.set(posuda.razina_svjetla)
        ent_razina_svjetla = tk.Entry(self, textvariable= ent_razina_svjetla_var, font=BODY_FONT, width=10)
        ent_razina_svjetla.grid(row= 6, column=1, padx=BODY_PADX, pady= BODY_PADY)
        ent_razina_svjetla.config(state= tk.DISABLED)
        
        ttk.Label(self, text='Biljka').grid(row= 7, column=0, padx=BODY_PADX, pady= BODY_PADY, sticky=tk.W)
        ent_biljka_var= tk.StringVar()
        l_id_biljke = posuda.id_biljke
        if l_id_biljke is not None:
            naziv_biljke = get_pybiljke_by_id(l_id_biljke).naziv
            ent_biljka_var.set(naziv_biljke)
        tk.Entry(self, textvariable= ent_biljka_var, font=BODY_FONT, width=10).grid(row= 7, column=1, padx=BODY_PADX, pady= BODY_PADY)

        def update_pot(posuda_id):
            nova_biljka = ent_biljka_var.get()
            if nova_biljka is None or nova_biljka == '':
                take_out_plant(posuda_id)
            else:
                update_biljka_posude(posuda_id, ent_naziv_posude_var.get(), ent_biljka_var.get() )
        btn_update_pot = ttk.Button(self, text='Ažuriraj/ Isprazni', command= partial(update_pot, posuda_id))
        btn_update_pot.grid(row= 8, column= 1, padx= BODY_PADX, pady= BODY_PADY)

        self.figure = Figure(figsize=(3,3),dpi=100)

    def create_graph(self, posuda_id):
            senzordata_df = pd.read_csv('db_data\pyposude.csv')
            var_graf = senzordata_df[['vlaga_zemlje','timestamp']].groupby('timestamp', as_index=False).sum() #,'ph_zemlje','temp_zraka',
            plot = self.figure.add_subplot(1,1,1)
            plot.hist(var_graf, 90)
            return plot.plot(var_graf['timestamp'], var_graf['vlaga_zemlje'])
            #plt.hist(var_graf, 25)

                