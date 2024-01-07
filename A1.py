import tkinter as tk
import random
import time

errors = [
    "Error 404: Girlfriend not found",
    "Critical error: Girlfriend has left the chat",
    "Error: Girlfriend.exe has stopped working",
    "Warning: Girlfriend's patience level has reached critical",
    "Error: Girlfriend's love not found",
    "Error: Girlfriend's expectations not met"
]

def display_error():
    while True:
        error_message = random.choice(errors)
        window = tk.Toplevel()
        window.title("Error")
        window.geometry(f"{window.winfo_screenwidth()//2}x{window.winfo_screenheight()//2}+{random.randint(0, 500)}+{random.randint(0, 500)}")
        label = tk.Label(window, text=error_message, font=("Arial", 50))
        label.pack(fill=tk.BOTH, expand=True)
        window.after(random.randint(1000, 5000), window.destroy)
        time.sleep(random.randint(1, 5))

        # Update the Tkinter event queue to display the window
        window.update()
        # Start the Tkinter event loop to allow the window to appear
        window.mainloop()

display_error()
