import tkinter as tk
from tkinter import ttk
from services.db_repo import get_all_pybiljke, insert_pybiljke
from constants import *
from models.biljka import Biljka
from .canvas_scroll import Scrollable
from .open_image import OpenImage

class TtkBiljke(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.frm_collection = []
    def list_pybiljke(self):
        btn_add_pot = ttk.Button(self, text='Dodaj biljku', width= 15, command= self.dodaj_biljku)
        btn_add_pot.pack(side='top', fill='y', pady= (10,0))
        frm_container = Scrollable(self)
        frm_container.pack( side='top', fill='x', expand= True)

        for biljka in get_all_pybiljke():
            frm_biljka = tk.Frame(frm_container.frm_scrollable, width=FRM_WIDTH)
            frm_biljka.pack( fill='x',  expand= True)
            frm_biljka.grid_columnconfigure((0,1), weight=2)

            lbl_biljka = tk.Label(frm_biljka, text=f'Naziv biljke: {biljka.naziv}')
            lbl_biljka.grid(row= 1, column=0, padx=BODY_PADX, pady= FIG_PADY, sticky=tk.W)
            l_njega = biljka.njega if biljka.njega is not None else ' '
            lbl_njega = tk.Label(frm_biljka, text=f'Biljci je potrebno: {l_njega}')
            lbl_njega.grid(row= 2, column=0, padx=BODY_PADX, pady= FIG_PADY, sticky=tk.W)

            naziv_posude = ''
            for r in biljka.posude:
                naziv_posude = naziv_posude + r.naziv + ', '
            lbl_posuda = tk.Label(frm_biljka, text=f'Biljka se nalazi u posudi: {naziv_posude}')
            lbl_posuda.grid(row= 3, column=0, padx=BODY_PADX, pady= FIG_PADY, sticky=tk.W)
            
            lbl_slika = OpenImage(frm_biljka, None, biljka.id)
            lbl_slika.grid(row= 1, column=1, rowspan=3, columnspan= 3, padx=BODY_PADX, pady= BODY_PADY, sticky=tk.E)   

            self.frm_collection.append(frm_biljka)
        
    def dodaj_biljku(self):
        save_window = tk.Toplevel(self)
        save_window.grid_columnconfigure((0,1), weight=1)
        ttk.Label(save_window, text='Naziv biljke').grid(row= 1, column=0, padx=BODY_PADX, pady= BODY_PADY, sticky=tk.W)
        ent_naziv_biljke_var = tk.StringVar()
        tk.Entry(save_window, textvariable= ent_naziv_biljke_var, font=BODY_FONT).grid(row= 1, column=1, padx=BODY_PADX, pady= BODY_PADY, sticky=tk.W)
        ttk.Label(save_window, text='Path slike').grid(row= 2, column=0, padx=BODY_PADX, pady= BODY_PADY, sticky=tk.W)
        ent_path_biljke_var = tk.StringVar()
        tk.Entry(save_window, textvariable= ent_path_biljke_var, font=BODY_FONT).grid(row= 2, column=1, padx=BODY_PADX, pady= BODY_PADY, sticky=tk.W)
        def spremi_biljku():
            biljka = Biljka(ent_naziv_biljke_var.get(), None)
            biljka.add_image(path= ent_path_biljke_var.get())
            insert_pybiljke(biljka)
            save_window.destroy()
        btn_spremi_biljku = ttk.Button(save_window, text='Spremi', command= spremi_biljku)
        btn_spremi_biljku.grid(row= 3, column=0, padx=BODY_PADX, pady= BODY_PADY, sticky=tk.W)
        

