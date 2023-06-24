from constants import *
from tk_gui.frm_login import *
from tk_gui.home_win import HomeWindow
from services.db_repo_init import db_init

#font=tk.font.nametofont('TkMenuFont')
#print(font.actual())

if __name__== '__main__':
    #db_init()
    #custom_image = tk.PhotoImage(file="naslovna.png").subsample(3,3)
    tk_app = HomeWindow()
  
    ''' print(f'iz maina je :{tk_app.frm_login.is_logged_in.get()}')
    if tk_app.frm_login.is_logged_in.get() is True:
        print(f'Idemo u novi frame')
        #main_frame.pack_forget()
        tk_app.lbl_footer.pack_forget()'''
    tk_app.mainloop()
