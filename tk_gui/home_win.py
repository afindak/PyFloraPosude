import tkinter as tk
from constants import *
from tk_gui.frm_login import *

class HomeWindow(tk.Tk):
    def __init__(self)-> None:
        super().__init__()
        self.title('PyFloraPosuda')
        self.geometry(INIT_WINDOW_SIZE)
        self.config(bg="black")
        main_frame = tk.LabelFrame(self, bg='black', text= 'Prijava', font=MENU_FONT, foreground='NavajoWhite2')
        main_frame.pack(padx=BODY_PADX, pady=ENT_PADY, fill='y')
        self.frm_login = FrmLogIn(main_frame)
        self.frm_login.pack(padx=BODY_PADX, pady=ENT_PADY, fill='y')
              

        footer_frame = tk.Frame(self, background='black')
        footer_frame.pack(padx= BODY_PADX, pady= ENT_PADY, fill='x')
        self.image = tk.PhotoImage(file="naslovna.png")
        self.custom_image = self.image.subsample(3,3)
        self.lbl_footer = tk.Label(footer_frame, image = self.custom_image)
        self.lbl_footer.pack(padx= BODY_PADX, pady= ENT_PADY, fill='y')
        