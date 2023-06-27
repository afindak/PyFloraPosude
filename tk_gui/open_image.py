import tkinter as tk
from services.db_repo import get_pybiljke_by_id, get_pyposude_by_id
from PIL import Image, ImageTk

class OpenImage(tk.Frame):
     def __init__(self, master, posuda_id):
        super().__init__(master)

        posuda = get_pyposude_by_id(posuda_id)
        if posuda.id_biljke is not None:
            file_biljke = get_pybiljke_by_id(posuda.id_biljke).show_image()
            image_file = Image.open(file_biljke).convert("RGB")
            resized= image_file.resize((100, 100), Image.ANTIALIAS)
            self.custom_image =  ImageTk.PhotoImage(resized)

            lbl_image = tk.Label(self, image = self.custom_image)
            lbl_image.grid(row=1, column=0, sticky= 'EW')