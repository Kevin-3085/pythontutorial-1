import tkinter as tk
from tkinter import messagebox

def convert():
    try:
        c = float(entry.get())
        f = (c * 9/5) + 32
        result_var.set(f"{f:.2f}")
    except:
        messagebox.showerror("Error", "Invalid Input")

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Convert", command=convert).pack()

result_var = tk.StringVar()
result = tk.Entry(root, textvariable=result_var, state='readonly')
result.pack()

root.mainloop()
