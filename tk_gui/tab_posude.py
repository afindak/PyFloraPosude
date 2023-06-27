import tkinter as tk
from tkinter import ttk
from services.db_repo import get_pyposude, update_pyposude, insert_pyposude, get_pyposude_by_id
from services.data_simulation import simul_data_for_pyposuda, save_sync_data
from functools import partial
from constants import *
from models.posuda import Posuda
from .canvas_scroll import Scrollable
from .open_pot import OpenPot
from .open_image import OpenImage

class TtkPosude(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.packing = []
        

    def list_pyposude(self):
        self.container = tk.Canvas(self, bg='#4A7A8C', width=FRM_WIDTH, height=25 )
        horizont_bar = tk.Scrollbar(self, orient='horizontal')
 
        self.container.grid(column=0, row=0, columnspan=8,  sticky='EW')
        horizont_bar.grid(row=2, column=0, sticky=tk.EW)
        self.container.configure(xscrollcommand= horizont_bar.set)
        horizont_bar.configure(command= self.container.xview)

        self.frm_container = tk.Frame(self.container, width=FRM_WIDTH, height=25)
        self.frm_container.grid(sticky= tk.NSEW, row= 0, column= 0, columnspan=8)

        btn_add_pot = ttk.Button(self.frm_container, text='Dodaj posudu', command= self.add_new_pot)
        btn_add_pot.grid(row= 0, column= 0, padx= BODY_PADX, pady= BODY_PADY)
        for i, posude in enumerate(get_pyposude(True)):
            btn_open_pot = ttk.Button(self.frm_container,text=f'{posude.naziv}', command=partial(self.open_pot, posude.id))
            btn_open_pot.grid(row= 0, column= f'{i+1}', padx=BODY_PADX, pady= BODY_PADY, sticky='e')
            self.packing.append(btn_open_pot)

        self.window = self.container.create_window((0, 0), window= self.frm_container, anchor=tk.NW)

        self.update_idletasks()
        self.container.bind('<Configure>', self.update_canvas)

        self.container.configure(scrollregion=self.frm_container.bbox(tk.ALL))
        self.container.configure(xscrollcommand= horizont_bar.set)
         
    def update_canvas(self, event):
            # if the new canvas's width (event.width) is larger than the content's 
            # minimum width (content.winfo_reqwidth()) then make canvas.frame the 
            # same width as the canvas
        if event.width > self.frm_container.winfo_reqwidth():
            self.container.itemconfigure(self.window, width=event.width)
    def open_pot(self, posuda_id):
        self.pack_forget ()    
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        frm_openpot = OpenPot( self, posuda_id)
        frm_openpot.grid(row=4, column=0, padx=BODY_PADX, pady= BODY_PADY, sticky= 'NS')
        
        btn_sync = ttk.Button(frm_openpot, text='SYNC', command= partial(self.sync_senzor_data, posuda_id))
        btn_sync.grid(row= 8, column=0, padx=BODY_PADX, pady= BODY_PADY)

        posuda = get_pyposude_by_id(posuda_id)
        if posuda.id_biljke is not None:
            frm_openimage = OpenImage(self, posuda_id= posuda_id)
            frm_openimage.grid(row=4, column=1, sticky='EW')
        else:
            self.pack_forget()

        #canvas= tk.Canvas(self, width= 100, height= 100)
        #canvas.grid(row=4, column=2, columnspan=3)
        #canvas.create_image(10,10, anchor=tk.NW, image=kaktus)
            
   
    def sync_senzor_data(self, posuda_id):
        vlaga_zemlje, ph_zemlje, temp_zraka, razina_svjetla = simul_data_for_pyposuda()
        save_sync_data(posuda_id, vlaga_zemlje, ph_zemlje, temp_zraka, razina_svjetla)
        update_pyposude(posuda_id, None, vlaga_zemlje, ph_zemlje, temp_zraka, razina_svjetla, None)
        self.open_pot(posuda_id)

    def add_new_pot(self):
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
        btn_save_pot.grid(row= 8, column=0, padx=BODY_PADX, pady= BODY_PADY)
       
    