# krestiki-noliki
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("300x350")


current_player = "X"
buttons = []

def on_click(row,col):
    pass

for i in range (3):
    row =[]
    for j in range(3):
        btn = tk.Button(window,text ="", font= ("Arial",20), width=5, height=2, command=lambda r=i, c=j: on_click(r,c))
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)


window.mainloop()
