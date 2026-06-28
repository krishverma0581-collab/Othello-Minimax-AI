import tkinter as tk
from tkinter import messagebox
from othello import *

root = tk.Tk()
root.title("Othello using Minimax AI")
root.geometry("1000x1300")
root.geometry("1000x1300+100+50")
root.lift()
root.attributes('-topmost', True)

board = create_board()
buttons = []

title = tk.Label(
    root,
    text="OTHELLO WITH MINIMAX AI",
    font=("Arial", 18, "bold")
)
title.grid(row=0, column=0, columnspan=9, pady=10)

# Score Labels
black_label = tk.Label(root, text="Black: 2", font=("Arial", 14))
black_label.grid(row=9, column=0, columnspan=4)
white_label = tk.Label(root, text="White: 2", font=("Arial", 14))
white_label.grid(row=9, column=4, columnspan=4)
status_label = tk.Label(
    root,
    text="Your Turn (Black)",
    font=("Arial", 14, "bold")
)
status_label.grid(row=10, column=0, columnspan=8)
def update_score():
    black, white = calculate_score(board)
    black_label.config(text=f"Black: {black}")
    white_label.config(text=f"White: {white}")


def update_board():

    valid_moves = get_valid_moves(board, 'B')

    for r in range(8):
        for c in range(8):

            if board[r][c] == 'B':
                buttons[r][c].config(
                    text='●',
                    bg='green',
                    fg='white'
                )

            elif board[r][c] == 'W':
                buttons[r][c].config(
                    text='○',
                    bg='green',
                    fg='white'
                )

            elif (r, c) in valid_moves:
                buttons[r][c].config(
                    text='',
                    bg='light green'
                )

            else:
                buttons[r][c].config(
                    text='',
                    bg='green'
                )

    update_score()

    if game_over(board):

        black, white = calculate_score(board)

        if black > white:
            winner = "Black Wins!"
        elif white > black:
            winner = "White Wins!"
        else:
            winner = "Match Draw!"

        messagebox.showinfo(
            "Game Over",
            f"Black: {black}\nWhite: {white}\n\n{winner}"
        )


def ai_turn():

    move = best_minimax_move(board, 'W', 3)

    if move is None:
        update_board()
        status_label.config(text="Your Turn (Black)")
        return

    make_move(board, move[0], move[1], 'W')
    update_board()

    status_label.config(text="Your Turn (Black)")

def player_move(r, c):

    if not is_valid_move(board, r, c, 'B'):
        messagebox.showwarning(
            "Invalid Move",
            "Please choose a highlighted square."
        )
        return

    status_label.config(text="AI Thinking...")

    make_move(board, r, c, 'B')
    update_board()

    root.after(500, ai_turn)


def restart_game():
    global board
    board = create_board()
    update_board()


# Create Board Buttons
for r in range(8):

    row = []

    for c in range(8):

        btn = tk.Button(
    root,
    width=3,
    height=1,
    bg='green',
    fg='white',
    font=('Arial', 18, 'bold'),
    command=lambda r=r, c=c: player_move(r, c)
)
        

        btn.grid(row=r+1, column=c+1)

        row.append(btn)

    buttons.append(row)


# Restart Button
restart_btn = tk.Button(
    root,
    text="Restart Game",
    font=("Arial", 12),
    command=restart_game
)

restart_btn.grid(
    row=11,
    column=0,
    columnspan=8,
    pady=15
)

update_board()

root.mainloop()