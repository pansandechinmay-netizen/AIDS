import tkinter as tk
from tkinter import messagebox
from collections import deque

# Goal state
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

board = list(goal)
buttons = []


def solve_bfs(start):
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [state]

        zero = state.index(0)
        row, col = divmod(zero, 3)

        moves = []

        if row > 0:
            moves.append(zero - 3)
        if row < 2:
            moves.append(zero + 3)
        if col > 0:
            moves.append(zero - 1)
        if col < 2:
            moves.append(zero + 1)

        for new_zero in moves:
            new_state = list(state)
            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            new_state = tuple(new_state)

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [state]))

    return None


def update_board():
    for i in range(9):
        buttons[i]["text"] = "" if board[i] == 0 else str(board[i])


def solve():
    start = tuple(board)
    solution = solve_bfs(start)

    if solution is None:
        messagebox.showinfo("Result", "No solution exists!")
        return

    # Display final solution
    for state in solution:
        print(state)

    board[:] = solution[-1]
    update_board()

    messagebox.showinfo(
        "Solved",
        f"Puzzle solved in {len(solution) - 1} moves!"
    )


# GUI window
root = tk.Tk()
root.title("8-Puzzle Solver")
root.geometry("400x450")

title = tk.Label(
    root,
    text="8-Puzzle Solver",
    font=("Arial", 24)
)
title.pack(pady=20)

frame = tk.Frame(root)
frame.pack()

# Create 3x3 buttons
for i in range(9):
    button = tk.Button(
        frame,
        text=str(board[i]) if board[i] != 0 else "",
        font=("Arial", 25),
        width=5,
        height=2
    )
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

solve_button = tk.Button(
    root,
    text="Solve Puzzle",
    font=("Arial", 16),
    command=solve
)
solve_button.pack(pady=30)

root.mainloop()
