import tkinter as tk
from services.db_repo import get_pybiljke_by_id, get_pyposude_by_id
from PIL import Image, ImageTk

class OpenImage(tk.Frame):
     def __init__(self, master, posuda_id, biljka_id = 0):
        super().__init__(master)

        if biljka_id != 0:
            l_biljka_id = biljka_id
        else:
            posuda = get_pyposude_by_id(posuda_id)
            l_biljka_id = posuda.id_biljke


        if l_biljka_id is not None:
            file_biljke = get_pybiljke_by_id(l_biljka_id).show_image()
            image_file = Image.open(file_biljke).convert("RGB")
            resized = image_file.resize((150, 150), Image.ANTIALIAS)
            self.custom_image =  ImageTk.PhotoImage(resized)
            #self.resized= custom_image.subsample(3,3)

            lbl_image = tk.Label(self, image = self.custom_image)
            lbl_image.grid(row=1, column=0, sticky= 'EW')