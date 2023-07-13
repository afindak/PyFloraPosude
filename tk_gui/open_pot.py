import tkinter as tk
from tkinter import ttk
from functools import partial
from constants import BODY_FONT, BODY_PADX, BODY_PADY
from datetime import datetime as dt
from services.db_repo import get_pybiljke_by_id, update_biljka_posude, take_out_plant, get_pyposude_by_id, get_all_pybiljke
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

class OpenPot(tk.Frame, ttk.Button):
    def __init__(self, master, posuda_id, btn_open_pot: ttk.Button ):
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
        if (l_id_biljke is not None) and l_id_biljke!= '':
            naziv_biljke = get_pybiljke_by_id(l_id_biljke).naziv
        else:
             naziv_biljke = None
        
        ent_biljka = ttk.Combobox(self, width= 12, textvariable= ent_biljka_var)
        values = [x.naziv for x in get_all_pybiljke()]
        ent_biljka['values'] = values
        ent_biljka.grid(row= 7, column=1, padx=BODY_PADX, pady= BODY_PADY)
        idx = values.index(naziv_biljke) if naziv_biljke is not None else None
        ent_biljka.current(idx)

        def update_pot(posuda_id, btn_open_pot):
            nova_biljka = ent_biljka_var.get()
            if nova_biljka is None or nova_biljka == '':
                take_out_plant(posuda_id, ent_naziv_posude_var.get())
            else:
                update_biljka_posude(posuda_id, ent_naziv_posude_var.get(), nova_biljka )
            btn_open_pot['text'] = ent_naziv_posude_var.get()
        btn_update_pot = ttk.Button(self, text='Ažuriraj/ Isprazni', command= partial(update_pot, posuda_id, btn_open_pot))
        btn_update_pot.grid(row= 8, column= 1, padx= BODY_PADX, pady= BODY_PADY)

        self.figure = plt.figure(figsize=(3,3),dpi=100)
    

    def create_graph(self, posuda_id):
            senzordata_df = pd.read_csv('db_data\pyposude.csv', sep=',')
            senzordata_df = senzordata_df.loc[(senzordata_df['posuda'] == posuda_id)]
            senzordata_df['timestamp'] = pd.to_datetime(senzordata_df['timestamp'])

            #self.figure, (graf1, graf2) = plt.subplots(1,2)
            graf1 = plt.subplot2grid((2,2),(0,0))
            graf2 = plt.subplot2grid((2,2),(0,1))
            graf3 = plt.subplot2grid((2,2),(1,0))
            
            graf1.set_ylabel('vlaga zemlje', fontsize = 8)
            graf2.set_ylabel('temperatura', fontsize = 8)
            graf3.set_ylabel('pH zemlje', fontsize = 8)

            graf1.plot(senzordata_df['timestamp'], senzordata_df['vlaga_zemlje'])
            locator = mdates.AutoDateLocator(minticks=3, maxticks=7)
            formatter = mdates.ConciseDateFormatter(locator) 
            graf1.xaxis.set_major_locator(locator)
            graf1.xaxis.set_major_formatter(formatter)
            # set font and rotation for date tick labels
            plt.gcf().autofmt_xdate()

            graf2.plot(senzordata_df['timestamp'], senzordata_df['temp_zraka'])
            graf2.xaxis.set_major_locator(locator)
            graf2.xaxis.set_major_formatter(formatter)

            graf3.plot(senzordata_df['timestamp'], senzordata_df['ph_zemlje'])
            graf3.xaxis.set_major_locator(locator)
            graf3.xaxis.set_major_formatter(formatter)

            plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
            return (self.figure, graf1, graf2, graf3)