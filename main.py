import tkinter as tk
from tkinter import *
from tkinter import ttk


# Game Logic
turn = "X"
turn_num = 0

def writev(s_num):
    global turn 
    global turn_num
    if s_num["text"] == "" and turn == "X":
        s_num["text"] = "X"
        turn = "O"
        turn_num += 1
        print(f"Turn number: {turn_num} ,Turn: {turn}")
    elif s_num["text"] == "" and turn == "O":
        s_num["text"] = "O"
        turn = "X"
        turn_num += 1
        print(f"Turn number: {turn_num} ,Turn: {turn}")
    win_vert()
    win_horizon()
    win_diag()
    check_draw()


 # Check win
def win_vert():
    if s1["text"] != "" and s1["text"] == s2["text"] == s3["text"]:
        title["text"] = f"{s1["text"]} win!"
        print(f"{s1["text"]} win!")
    elif s4["text"] != "" and s4["text"] == s5["text"] == s6["text"]:
        title["text"] = f"{s4["text"]} win!"
        print(f"{s4["text"]} win!")
    elif s7["text"] != "" and s7["text"] == s8["text"] == s9["text"]:
        title["text"] = f"{s7["text"]} win!"
        print(f"{s7["text"]} win!")

def win_horizon():
    if s1["text"] != "" and s1["text"] == s4["text"] == s7["text"]:
        title["text"] = f"{s1["text"]} win!"
        print(f"{s1["text"]} win!")
    elif s2["text"] != "" and s2["text"] == s5["text"] == s8["text"]:
        title["text"] = f"{s2["text"]} win!"
        print(f"{s2["text"]} win!")
    elif s3["text"] != "" and s3["text"] == s6["text"] == s9["text"]:
        title["text"] = f"{s3["text"]} win!"
        print(f"{s3["text"]} win!")

def win_diag():
    if s1["text"] != "" and s1["text"] == s5["text"] == s9["text"]:
        title["text"] = f"{s1["text"]} win!"
        print(f"{s1["text"]} win!")
    elif s3["text"] != "" and s3["text"] == s5["text"] == s7["text"]:
        title["text"] = f"{s3["text"]} win!"
        print(f"{s3["text"]} win!")

# Check for draw
def check_draw():
    global turn_num
    if turn_num == 9 and title["text"] == "X&O Game":
        title["text"] = "Draw!"
        print("Draw!")


# Reset the game
def reset_game():
    global turn, turn_num
    turn = "X"
    turn_num = 0
    title["text"] = "X&O Game"
    s1["text"] = ""
    s2["text"] = ""
    s3["text"] = ""
    s4["text"] = ""
    s5["text"] = ""
    s6["text"] = ""
    s7["text"] = ""
    s8["text"] = ""
    s9["text"] = ""
    print("Game reset!")


# GUI
window = tk.Tk()
window.title("X&O Game")
window.geometry("420x550")
# window.iconbitmap("tic-tac-toe.ico")
game_frame = tk.Frame(window)
game_frame.place(relx=0.5, rely=0.6, anchor='center')


control_frame = tk.Frame(window)
control_frame.place(relx=0.5, rely=0.6, anchor='center')
title = tk.Label(game_frame, text="X&O Game" , font=("Arial", 20))
title.grid(row=0, column=0, columnspan=3, pady=(0, 10))
# .place(anchor='center', rely=0.0)
# title.grid(pady=10, padx=10)

s1 = tk.Button(game_frame, text="" ,width=9, height=4 ,font=("Arial", 10), command= lambda: writev(s1))
s1.grid(row=1, column=0, padx=3, pady=3)
s2 = tk.Button(game_frame, text="" ,width=9, height=4 ,font=("Arial", 10), command= lambda: writev(s2))
s2.grid(row=1, column=1 , padx=3, pady=3)
s3 = tk.Button(game_frame, text="" ,width=9, height=4 ,font=("Arial", 10), command= lambda: writev(s3))
s3.grid(row=1, column=2, padx=3, pady=3)

s4 = tk.Button(game_frame, text="" ,width=9, height=4 ,font=("Arial", 10), command= lambda: writev(s4))
s4.grid(row=2, column=0, padx=3, pady=3)
s5 = tk.Button(game_frame, text="" ,width=9, height=4 ,font=("Arial", 10), command= lambda: writev(s5))
s5.grid(row=2, column=1, padx=3, pady=3)
s6 = tk.Button(game_frame, text="" ,width=9, height=4 ,font=("Arial", 10), command= lambda: writev(s6))
s6.grid(row=2, column=2, padx=3, pady=3)

s7 = tk.Button(game_frame, text="" ,width=9, height=4 ,font=("Arial", 10), command= lambda: writev(s7))
s7.grid(row=3, column=0, padx=3, pady=3)
s8 = tk.Button(game_frame, text="" ,width=9, height=4 ,font=("Arial", 10), command= lambda: writev(s8))
s8.grid(row=3, column=1, padx=3, pady=3)
s9 = tk.Button(game_frame, text="" ,width=9, height=4 ,font=("Arial", 10), command= lambda: writev(s9))
s9.grid(row=3, column=2, padx=3, pady=3)
space = tk.Label(game_frame,text="  ", font=("Arial", 40)).grid(row=5, column=0)

resetb = tk.Button(game_frame, text="Reset" ,width=9, height=2, font=("Arial", 13) , command= lambda: reset_game()).grid(row=6 ,column=0)

# game = s1, s2, s3, s4, s5, s6, s7, s8, s9
# game.config(font=("Arial", 20))

window.mainloop()
