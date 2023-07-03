import tkinter as tk
from tkinter import ttk
from constants import BODY_FONT, BODY_PADX, BODY_PADY
from services.db_repo import get_user_by_username, update_user
from functools import partial

class TtkMojProfil(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.user = get_user_by_username('afindak')

        #self.grid_columnconfigure((0,1), weight=1)
        
        lbl_username = tk.Label(self, text= 'Username', font= BODY_FONT)
        lbl_username.grid(row= 1, column= 0, padx= BODY_PADX, pady= BODY_PADY, sticky= tk.W)

        self.ent_username_var = tk.StringVar()
        self.ent_username_var.set(self.user.username) 
        ent_username = tk.Entry(self, textvariable= self.ent_username_var, font= BODY_FONT)
        ent_username.grid(row= 1, column= 1, padx= BODY_PADX, pady= BODY_PADY, sticky= tk.W)
        ent_username.config(state= tk.DISABLED)

        lbl_password = tk.Label(self, text='New password', font= BODY_FONT)
        lbl_password.grid(row= 2, column= 0, padx= BODY_PADX, pady= BODY_PADY, sticky= tk.W)

        self.ent_password_var = tk.StringVar()
        ent_password = tk.Entry(self, textvariable= self.ent_password_var, font= BODY_FONT)
        ent_password.grid(row= 2, column= 1, padx= BODY_PADX, pady= BODY_PADY, sticky= tk.W)

        lbl_ime = tk.Label(self, text= 'Ime', font= BODY_FONT)
        lbl_ime.grid(row= 3, column= 0, padx= BODY_PADX, pady= BODY_PADY, sticky= tk.W)

        self.ent_ime_var = tk.StringVar()
        self.ent_ime_var.set(self.user.ime) 
        ent_ime = tk.Entry(self, textvariable= self.ent_ime_var, font= BODY_FONT)
        ent_ime.grid(row= 3, column= 1, padx= BODY_PADX, pady= BODY_PADY, sticky= tk.W)
        
        lbl_prezime = tk.Label(self, text='Prezime', font= BODY_FONT)
        lbl_prezime.grid(row= 4, column= 0, padx= BODY_PADX, pady= BODY_PADY, sticky= tk.W)

        self.ent_prezime_var = tk.StringVar()
        self.ent_prezime_var.set(self.user.prezime) 
        ent_prezime = tk.Entry(self, textvariable= self.ent_prezime_var, font= BODY_FONT)
        ent_prezime.grid(row= 4, column= 1, padx= BODY_PADX, pady= BODY_PADY, sticky= tk.W)

        btn_update = tk.Button(self, text='Ažuriraj', command= partial(self.update_profile, self.user.username))
        btn_update.grid(row= 5, column= 1, padx= BODY_PADX, pady= BODY_PADY)

    def update_profile(self, username):
        l_ime = self.ent_ime_var.get()
        l_prezime = self.ent_prezime_var.get()
        l_password = self.ent_password_var.get()
        update_user(username, l_ime, l_prezime, l_password)

        