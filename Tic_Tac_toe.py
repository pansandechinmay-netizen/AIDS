import tkinter as tk
from tkinter import messagebox

# Create window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("400x450")

player = "X"
board = [""] * 9


def check_winner():
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] != "":
            return True

    return False


def button_click(index):
    global player

    # Ignore already occupied button
    if board[index] != "":
        return

    board[index] = player
    buttons[index]["text"] = player

    # Check winner
    if check_winner():
        messagebox.showinfo("Game Over", f"Player {player} wins!")
        root.destroy()
        return

    # Check draw
    if "" not in board:
        messagebox.showinfo("Game Over", "It's a draw!")
        root.destroy()
        return

    # Change player
    player = "O" if player == "X" else "X"
    label.config(text=f"Player {player}'s Turn")


# Title
label = tk.Label(root, text="Player X's Turn", font=("Arial", 20))
label.pack(pady=20)

# Create buttons
frame = tk.Frame(root)
frame.pack()

buttons = []

for i in range(9):
    button = tk.Button(
        frame,
        text="",
        font=("Arial", 30),
        width=5,
        height=2,
        command=lambda i=i: button_click(i)
    )

    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

root.mainloop()
