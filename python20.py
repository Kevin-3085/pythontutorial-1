import tkinter as tk

def bill():
    try:
        price = float(p.get())
        qty = int(q.get())

        total = price * qty

        if total > 1000:
            total *= 0.9   # 10% discount

        result.set(f"{total:.2f}")
    except:
        result.set("Invalid Input")

root = tk.Tk()

p = tk.Entry(root)
p.pack()

q = tk.Entry(root)
q.pack()

tk.Button(root, text="Generate Bill", command=bill).pack()

result = tk.StringVar()
tk.Entry(root, textvariable=result).pack()

root.mainloop()
