from tk_gui.home_win import HomeWindow
from services.db_repo_init import db_init

if __name__== '__main__':
    db_init()
    tk_app = HomeWindow()

    tk_app.mainloop()
