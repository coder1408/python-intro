import tkinter as tk
from tkinter import messagebox

def ask_valentine():
    result = messagebox.askquestion("Will you be my Valentine?", "Really? I'll ask you again, Will you be my Valentine!?")
    if result == "yes":
        messagebox.showinfo("Response", "Wow! I'm so happy! ❤️❤️❤️")
    else:
        messagebox.showwarning("Response", "Okay, I'll ask someone else then!!")

root = tk.Tk()
root.withdraw()
result = messagebox.askquestion("Will you be my Valentine?", "Will you be my Valentine?")
if result == "no":
    root.after(0, ask_valentine)
else:
    messagebox.showinfo("Response", "Wow! I'm so happy! ❤️❤️❤️")
root.mainloop()
