import tkinter as tk
from tkinter import messagebox

def choose_symbol(symbol):
    global current_player
    current_player = symbol
    start_window.destroy()

def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            return True
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            return True
    
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return True
    return False

def check_draw():
    for row in buttons:
        for btn in row:
            if btn['text'] == "":
                return False
    return True

def on_click(row, col):
    global current_player

    if buttons[row][col]['text'] != "":
        return
    buttons[row][col]['text'] = current_player
    buttons[row][col]['fg'] = "red"

    if check_winner():
        messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")
        window.quit()
    elif check_draw():
        messagebox.showinfo("Игра окончена", "СЕГОДНЯ ПОБЕДИТЕЛЕЙ НЕТ")
        window.quit()
    else:
        current_player = 'O' if current_player == 'X' else 'X'

# Окно выбора символа
start_window = tk.Tk()
start_window.title("Выбор символа")
start_window.geometry("300x150")
tk.Label(start_window, text="Выберите символ для игры", font=("Arial", 14)).pack(pady=10)
tk.Button(start_window, text="X", font=("Arial", 14), width=5, command=lambda: choose_symbol("X")).pack(side=tk.LEFT, padx=20)
tk.Button(start_window, text="O", font=("Arial", 14), width=5, command=lambda: choose_symbol("O")).pack(side=tk.RIGHT, padx=20)
start_window.mainloop()

# Главное игровое окно
window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("300x350")
window.configure(bg="lightblue")

buttons = []
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2, fg="black", command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)

window.mainloop()

