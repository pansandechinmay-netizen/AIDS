
import tkinter as tk
from tkinter import messagebox
from collections import deque

# Jug capacities
JUG1 = 4
JUG2 = 3
TARGET = 2


# BFS function
def solve_bfs():
    start = (0, 0)

    # Queue for BFS
    queue = deque([start])

    # Visited states
    visited = {start}

    # Store parent of each state
    parent = {start: None}

    while queue:
        current = queue.popleft()
        a, b = current

        # Check whether the target is reached
        if a == TARGET or b == TARGET:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            show_solution(path)
            return

        # Possible operations
        states = [
            (JUG1, b),  # Fill Jug 1
            (a, JUG2),  # Fill Jug 2
            (0, b),     # Empty Jug 1
            (a, 0),     # Empty Jug 2

            # Pour Jug 1 into Jug 2
            (
                a - min(a, JUG2 - b),
                b + min(a, JUG2 - b)
            ),

            # Pour Jug 2 into Jug 1
            (
                a + min(b, JUG1 - a),
                b - min(b, JUG1 - a)
            )
        ]

        # Add unvisited states to the queue
        for state in states:
            if state not in visited:
                visited.add(state)
                queue.append(state)
                parent[state] = current

    messagebox.showinfo("Result", "No solution exists!")


# Display solution
def show_solution(path):
    solution_text.config(state=tk.NORMAL)
    solution_text.delete("1.0", tk.END)

    solution_text.insert(
        tk.END,
        "BFS SOLUTION\n"
        "============\n\n"
    )

    for i, state in enumerate(path):
        solution_text.insert(
            tk.END,
            f"Step {i}: Jug 1 = {state[0]} L, "
            f"Jug 2 = {state[1]} L\n"
        )

    solution_text.insert(
        tk.END,
        "\nGoal Reached: Exactly 2 Litres!"
    )

    solution_text.config(state=tk.DISABLED)


# Clear solution
def clear_solution():
    solution_text.config(state=tk.NORMAL)
    solution_text.delete("1.0", tk.END)
    solution_text.config(state=tk.DISABLED)


# ---------------- GUI ----------------

root = tk.Tk()
root.title("Water Jug Problem - BFS")
root.geometry("600x500")
root.resizable(False, False)

# Title
title = tk.Label(
    root,
    text="WATER JUG PROBLEM",
    font=("Arial", 22, "bold")
)
title.pack(pady=15)

# Problem information
info = tk.Label(
    root,
    text="Jug 1 = 4 Litres  |  Jug 2 = 3 Litres\n"
         "Goal: Measure exactly 2 Litres",
    font=("Arial", 14)
)
info.pack(pady=10)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack(pady=15)

# Solve button
solve_button = tk.Button(
    button_frame,
    text="SOLVE USING BFS",
    font=("Arial", 12, "bold"),
    width=18,
    command=solve_bfs
)
solve_button.pack(side=tk.LEFT, padx=5)

# Clear button
clear_button = tk.Button(
    button_frame,
    text="CLEAR",
    font=("Arial", 12),
    width=10,
    command=clear_solution
)
clear_button.pack(side=tk.LEFT, padx=5)

# Solution display
solution_text = tk.Text(
    root,
    width=55,
    height=15,
    font=("Courier New", 11),
    wrap=tk.WORD
)
solution_text.pack(pady=10)
solution_text.config(state=tk.DISABLED)

# Start GUI
root.mainloop()
