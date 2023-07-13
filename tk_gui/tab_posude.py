import tkinter as tk
from tkinter import ttk
from services.db_repo import get_pyposude, update_pyposude, insert_pyposude, get_pyposude_by_id, update_pybiljke, get_biljka_from_naziv, get_all_pybiljke
from services.data_simulation import simul_data_for_pyposuda, save_sync_data, get_njega
from functools import partial
from constants import *
from models.posuda import Posuda
from .open_pot import OpenPot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class TtkPosude(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.packing = []
        self.len_posude = 1

    def list_pyposude(self):
        self.container = tk.Canvas(self, width=FRM_WIDTH, height=25 )
        horizont_bar = tk.Scrollbar(self, orient='horizontal')
 
        self.container.grid(column=0, row=0, columnspan=8,  sticky='EW')
        horizont_bar.grid(row=2, column=0, sticky=tk.EW)
        
        self.frm_container = tk.Frame(self.container, width=FRM_WIDTH, height=25)
        self.frm_container.grid(sticky= tk.NSEW, row= 0, column= 0, columnspan=8)

        btn_add_pot = ttk.Button(self.frm_container, text='Dodaj posudu', command= self.add_new_pot)
        btn_add_pot.grid(row= 0, column= 0, padx= BODY_PADX, pady= BODY_PADY)
        for i, posude in enumerate(get_pyposude(True)):
            self.btn_open_pot = ttk.Button(self.frm_container,text=f'{posude.naziv}', command=partial(self.open_pot, posude.id))
            self.btn_open_pot.grid(row= 0, column= f'{i+1}', padx=BODY_PADX, pady= BODY_PADY, sticky='e')
            self.packing.append((posude.id, self.btn_open_pot))
            self.len_posude += 1

        self.window = self.container.create_window((0, 0), window= self.frm_container, anchor=tk.NW)
        self.update_idletasks()
        self.container.bind('<Configure>', self.update_canvas)
        self.container.configure(scrollregion=self.frm_container.bbox(tk.ALL))
        self.container.configure(xscrollcommand= horizont_bar.set)
        horizont_bar.configure(command= self.container.xview)
         
    def update_canvas(self, event):
        if event.width > self.frm_container.winfo_reqwidth():
            self.container.itemconfigure(self.window, width=event.width)

    def open_pot(self, posuda_id):
        self.pack_forget ()    
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        #posuda = get_pyposude_by_id(posuda_id)
        for r in self.packing:
            if r[0] == posuda_id:
                l_button = r[1]
        frm_openpot = OpenPot( self, posuda_id, l_button)
        frm_openpot.grid(row=4, column=0, padx=BODY_PADX, pady= BODY_PADY, sticky= 'W')
        
        btn_sync = ttk.Button(frm_openpot, text='SYNC', command= partial(self.sync_senzor_data, posuda_id))
        btn_sync.grid(row= 8, column=0, padx=BODY_PADX, pady= BODY_PADY, sticky= 'W')

        graph = frm_openpot.create_graph(posuda_id)
        canvas = FigureCanvasTkAgg(frm_openpot.figure, self)
        canvas.get_tk_widget().grid(row=4, column=1, sticky= 'EW')

        #OpenImage(self, posuda_id= posuda_id).grid(row=4, column=1, sticky='EW')
        #canvas= tk.Canvas(self, width= 100, height= 100)
        #canvas.grid(row=4, column=2, columnspan=3)
        #canvas.create_image(10,10, anchor=tk.NW, image=kaktus)

    def sync_senzor_data(self, posuda_id):
        vlaga_zemlje, ph_zemlje, temp_zraka, razina_svjetla = simul_data_for_pyposuda()
        save_sync_data(posuda_id, vlaga_zemlje, ph_zemlje, temp_zraka, razina_svjetla)
        update_pyposude(posuda_id, None, vlaga_zemlje, ph_zemlje, temp_zraka, razina_svjetla, None)
        
        posuda = get_pyposude_by_id(posuda_id)
        biljka_id = posuda.id_biljke
        if biljka_id:
            njega = get_njega(posuda_id)
            update_pybiljke(biljka_id, None, None, njega)
        self.open_pot(posuda_id)

    def add_new_pot(self):
        save_window = tk.Toplevel(self)
        ttk.Label(save_window, text='Naziv posude').grid(row= 1, column=0, padx=BODY_PADX, pady= BODY_PADY, sticky=tk.W)
        ent_naziv_posude_var = tk.StringVar()
        tk.Entry(save_window, textvariable= ent_naziv_posude_var, font=BODY_FONT).grid(row= 1, column=1, padx=BODY_PADX, pady= BODY_PADY, sticky=tk.W)
        ttk.Label(save_window, text='Naziv biljke').grid(row= 2, column=0, padx=BODY_PADX, pady= BODY_PADY, sticky=tk.W)

        biljka_var = tk.StringVar()
        ent_biljka = ttk.Combobox(save_window, width= 20, textvariable= biljka_var)
        values = [x.naziv for x in get_all_pybiljke()]
        ent_biljka['values'] = values
        ent_biljka.grid(row= 2, column=1, padx=BODY_PADX, pady= BODY_PADY, sticky=tk.W)

        def save_pot():
            biljka_id = get_biljka_from_naziv(biljka_var.get())
            posuda = Posuda(ent_naziv_posude_var.get(),None,None,None,None,biljka_id)
            id_posude = insert_pyposude(posuda)
            self.btn_open_pot = ttk.Button(self.frm_container,text= ent_naziv_posude_var.get(), command=partial(self.open_pot, id_posude))
            self.btn_open_pot.grid(row= 0, column= f'{self.len_posude+1}', padx=BODY_PADX, pady= BODY_PADY, sticky='e')
            self.len_posude +=1
            self.packing.append((id_posude, self.btn_open_pot))
            self.update_idletasks()
            self.container.bind('<Configure>', self.update_canvas)
            self.container.configure(scrollregion=self.frm_container.bbox(tk.ALL))
            save_window.destroy()
        btn_save_pot = ttk.Button(save_window, text='Spremi', command= save_pot)
        btn_save_pot.grid(row= 3, column=0, padx=BODY_PADX, pady= BODY_PADY, sticky=tk.W)

       
    