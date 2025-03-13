import tkinter as tk
from tkinter import messagebox
from infix_to_postfix import infix_to_postfix
from postfix import evaluate_postfix

def convert_expression():
    expression = entry.get()
    try:
        postfix_expr = infix_to_postfix(expression)
        postfix_var.set(postfix_expr)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to convert expression: {e}")

def evaluate_expression():
    postfix_expr = postfix_var.get()
    try:
        result = evaluate_postfix(postfix_expr)
        result_var.set(result)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to evaluate expression: {e}")

# UI Setup
root = tk.Tk()
root.title("Infix to Postfix Calculator")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(pady=20)

tk.Label(frame, text="Enter Infix Expression:").grid(row=0, column=0)
entry = tk.Entry(frame, width=30)
entry.grid(row=0, column=1)

tk.Button(frame, text="Convert", command=convert_expression).grid(row=0, column=2)

postfix_var = tk.StringVar()
tk.Label(frame, text="Postfix Expression:").grid(row=1, column=0)
postfix_entry = tk.Entry(frame, textvariable=postfix_var, state='readonly', width=30)
postfix_entry.grid(row=1, column=1)

tk.Button(frame, text="Evaluate", command=evaluate_expression).grid(row=1, column=2)

result_var = tk.StringVar()
tk.Label(frame, text="Result:").grid(row=2, column=0)
result_entry = tk.Entry(frame, textvariable=result_var, state='readonly', width=30)
result_entry.grid(row=2, column=1)

root.mainloop()
