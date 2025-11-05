# Digital Clock using Tkinter
import tkinter as tk
from time import strftime

# Create window
root = tk.Tk()
root.title("🕒 Digital Clock")
root.geometry("400x200")
root.resizable(False, False)
root.configure(bg="#0A0A0A")

# Clock display
label_time = tk.Label(
    root,
    font=("Helvetica", 50, "bold"),
    background="#0A0A0A",
    foreground="#00FF00"
)
label_time.pack(anchor="center", pady=20)

# Date display
label_date = tk.Label(
    root,
    font=("Helvetica", 20),
    background="#0A0A0A",
    foreground="#FFFFFF"
)
label_date.pack(anchor="s")

# Function to update time & date
def update():
    current_time = strftime("%I:%M:%S %p")  # Hour:Minute:Second AM/PM
    current_date = strftime("%A, %d %B %Y") # Day, Date Month Year
    label_time.config(text=current_time)
    label_date.config(text=current_date)
    label_time.after(1000, update)  # refresh every 1 sec

update()
root.mainloop()
