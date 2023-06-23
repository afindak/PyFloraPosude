import tkinter as tk
from constants import *
from services.db_repo import get_user_by_username
from .tab_control import MainWindow

''''class MyProfile():
    def __init__(self, username = '', password = '', is_loggedin = False):
        self.username = username
        self.password = password
        self.is_loggedin = is_loggedin'''


class FrmLogIn(tk.Frame):
    def __init__(self, master )-> None:
        super().__init__(master, background='black')
        self.is_logged_in = tk.BooleanVar()

        lbl_username = tk.Label(self, text='Username', font= MENU_FONT, background='NavajoWhite3', foreground='gray18')
        lbl_username.grid(row=0, column=0,padx= BODY_PADX, pady= BODY_PADY, sticky='ew' )

        self.ent_username_var = tk.StringVar()
        ent_username = tk.Entry(self, textvariable= self.ent_username_var, font= MENU_FONT, background= 'NavajoWhite4', foreground='NavajoWhite2')
        ent_username.grid(row=0, column=1, padx=BODY_PADX, pady= BODY_PADY, sticky='ew')

        lbl_password = tk.Label(self, text='Password', font= MENU_FONT, background='NavajoWhite3', foreground='gray18')
        lbl_password.grid(row=1, column=0,padx= BODY_PADX, pady= BODY_PADY, sticky='ew' )

        self.ent_password_var = tk.StringVar()
        ent_password = tk.Entry(self, textvariable= self.ent_password_var, font= MENU_FONT, background= 'NavajoWhite4', foreground='NavajoWhite2')
        ent_password.grid(row=1, column=1, padx=BODY_PADX, pady= BODY_PADY, sticky='ew')
       
        self.btn_log_in = tk.Button(self, text='Log in', width=10, font= MENU_FONT, command= self.logging, background='NavajoWhite3', foreground='gray18')
        self.btn_log_in.grid(row=2, column=1, padx=BODY_PADX, pady= BODY_PADY, sticky='e')
        
        self.lbl_login_failed = tk.Label(self, text='Nepoznat korisnik. Prijava nije uspjela.', font= MENU_FONT, background='NavajoWhite3', foreground='gray18')

    def all_children (self) :
        _list = self.master.master.winfo_children()
        '''for item in _list :
            if self.master.master.winfo_children() :
                _list.extend(item.winfo_children())'''
        return _list

        
    def logging(self):
        username = self.ent_username_var.get()
        password = self.ent_password_var.get()
        if (username !='' and password !=''):
            user = get_user_by_username(username)
            if user.password == password:
                print('done')
                #self.master.pack_forget()
                self.is_logged_in.set(True)
                widget_list = [item.pack_forget() for item in self.all_children()]
                new_frame = tk.Frame(self.master.master, bg='black')
                new_frame.pack(padx=BODY_PADX, pady=BODY_PADY, fill='y')
                tab_frame = MainWindow(new_frame)
                tab_frame.pack(padx= BODY_PADX, pady= BODY_PADY, fill='both')
            else:
                self.lbl_login_failed.grid(row=3, column=1, padx=BODY_PADX, pady= BODY_PADY, sticky='e')