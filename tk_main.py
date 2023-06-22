import tkinter as tk
import tkinter.font
from constants import *
from models.korisnik import Korisnik
from services.db_repo import get_user_by_username

def logging():
    global user
    username = ent_username_var.get()
    password = ent_password_var.get()
    if (username !='' and password !=''):
        user = get_user_by_username(username)
        if user.password == password:
            print('done')
            main_frame.pack_forget()
            footer_frame.pack_forget()
    else:
        lbl_login_failed.grid(row=3, column=1, padx=BODY_PADX, pady= BODY_PADY, sticky='e')

main_window = tk.Tk()

main_window.title('PyFloraPosuda')
main_window.geometry(INIT_WINDOW_SIZE)
main_window.config(bg="black")

main_frame = tk.LabelFrame(main_window,bg='black', text= 'Prijava', font=MENU_FONT, foreground='NavajoWhite2')
main_frame.pack(padx=BODY_PADX, pady=BODY_PADY, fill='y')

lbl_username = tk.Label(main_frame, text='Username', font= MENU_FONT, background='NavajoWhite3', foreground='gray18')
lbl_username.grid(row=0, column=0,padx= 5, pady= 10, sticky='ew' )

ent_username_var = tk.StringVar()
ent_username = tk.Entry(main_frame, textvariable= ent_username_var, font= MENU_FONT, background= 'NavajoWhite4', foreground='NavajoWhite2')
ent_username.grid(row=0, column=1, padx=BODY_PADX, pady= BODY_PADY, sticky='ew')

lbl_password = tk.Label(main_frame, text='Password', font= MENU_FONT, background='NavajoWhite3', foreground='gray18')
lbl_password.grid(row=1, column=0,padx= BODY_PADX, pady= BODY_PADY, sticky='ew' )

ent_password_var = tk.StringVar()
ent_password = tk.Entry(main_frame, textvariable= ent_password_var, font= MENU_FONT, background= 'NavajoWhite4', foreground='NavajoWhite2')
ent_password.grid(row=1, column=1, padx=BODY_PADX, pady= BODY_PADY, sticky='ew')

btn_log_in = tk.Button(main_frame, text='Prijavi me', font= MENU_FONT, command= logging, background='NavajoWhite3', foreground='gray18')
btn_log_in.grid(row=2, column=1, padx=BODY_PADX, pady= BODY_PADY, sticky='e')

lbl_login_failed = tk.Label(main_frame, text='Nepoznat korisnik. Prijava nije uspjela.', font= MENU_FONT, background='NavajoWhite3', foreground='gray18')

footer_frame = tk.Frame(main_window, background='black')
footer_frame.pack(padx= BODY_PADX, pady= BODY_PADY, fill='x')
image = tk.PhotoImage(file="naslovna.png")
custom_image = image.subsample(3,3)
tk.Label(footer_frame, image = custom_image).pack(padx= BODY_PADX, pady= BODY_PADY, fill='y')



#font=tk.font.nametofont('TkMenuFont')
#print(font.actual())
main_window.mainloop()