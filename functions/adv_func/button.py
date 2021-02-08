import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()




button = tk.Button(frame, text="click me", fg="black", command=lambda: print('hello'))



button.pack(side=tk.LEFT)
root.mainloop()