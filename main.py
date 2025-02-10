import tkinter as tk
from tkinter import messagebox

def choose_symbol(symbol):
    global current_player, player_scores
    current_player = symbol
    player_scores = {'X': 0, 'O': 0}
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
        player_scores[current_player] += 1
        update_score_label()
        messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")
        reset_board()
    elif check_draw():
        messagebox.showinfo("Игра окончена", "НИКТО НЕ ВЫИГРАЛ. НИЧЬЯ")
        reset_board()
    else:
        current_player = 'O' if current_player == 'X' else 'X'

def reset_board():
    """Очищает игровое поле, но не сбрасывает счет"""
    for row in buttons:
        for btn in row:
            btn['text'] = ""
    global current_player
    current_player = 'X'

def reset_game():
    """Полностью сбрасывает игру (включая счет)"""
    global player_scores
    player_scores = {'X': 0, 'O': 0}
    update_score_label()
    reset_board()

def update_score_label():
    score_label.config(text=f"Счет: X - {player_scores['X']} | O - {player_scores['O']}")

# Окно выбора символа
start_window = tk.Tk()
start_window.title("Выбор символа")
start_window.geometry("300x200")

tk.Label(start_window, text="ИГРА ДЛЯ 2 УЧАСТНИКОВ", font=("Arial", 14, "bold"), fg="blue").pack(pady=5)
tk.Label(start_window, text="Выберите символ для игры", font=("Arial", 14)).pack(pady=10)
tk.Button(start_window, text="X", font=("Arial", 14), width=5, command=lambda: choose_symbol("X")).pack(side=tk.LEFT, padx=20)
tk.Button(start_window, text="O", font=("Arial", 14), width=5, command=lambda: choose_symbol("O")).pack(side=tk.RIGHT, padx=20)

start_window.mainloop()

# Главное игровое окно
window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("300x450")
window.configure(bg="lightblue")

score_label = tk.Label(window, text="Счет: X - 0 | O - 0", font=("Arial", 14), bg="lightblue")
score_label.grid(row=0, column=0, columnspan=3, pady=5)

buttons = []
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2, fg="black", command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i+1, column=j)  # Смещаем кнопки вниз, чтобы освободить место для счета
        row.append(btn)
    buttons.append(row)

tk.Button(window, text="Сбросить партию", font=("Arial", 14), command=reset_board).grid(row=4, column=0, columnspan=3, pady=5)
tk.Button(window, text="Сбросить игру", font=("Arial", 14), command=reset_game).grid(row=5, column=0, columnspan=3, pady=5)

window.mainloop()

