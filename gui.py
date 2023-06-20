import tkinter as tk
posude = []

root = tk.Tk()
root.geometry('600x400')
root.title('Pyflora')

if posude:
    for i, posuda in enumerate(posude):
        tk.Label(text=f'Posuda {i} - {posuda}').pack()
else:
    tk.Label(text='Nema posude').pack()

btn_add_pot = tk.Button(text='Dodaj novu posudu')
btn_add_pot.pack()

root.mainloop()