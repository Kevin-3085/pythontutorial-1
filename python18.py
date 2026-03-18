import tkinter as tk
from tkinter import messagebox

def calculate(op):
    try:
        a = int(e1.get())
        b = int(e2.get())

        if op == "add":
            res = a + b
        elif op == "sub":
            res = a - b
        elif op == "mul":
            res = a * b
        elif op == "div":
            res = a / b

        result_var.set(res)

    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero")
    except:
        messagebox.showerror("Error", "Invalid Input")

root = tk.Tk()

e1 = tk.Entry(root)
e1.pack()

e2 = tk.Entry(root)
e2.pack()

result_var = tk.StringVar()

tk.Button(root, text="Add", command=lambda: calculate("add")).pack()
tk.Button(root, text="Subtract", command=lambda: calculate("sub")).pack()
tk.Button(root, text="Multiply", command=lambda: calculate("mul")).pack()
tk.Button(root, text="Divide", command=lambda: calculate("div")).pack()

tk.Entry(root, textvariable=result_var).pack()

root.mainloop()
