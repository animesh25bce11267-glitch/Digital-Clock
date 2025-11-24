import tkinter as tk
import time

# ---------------------------
# Aesthetic Digital Clock App
# ---------------------------

def update_clock():
    current_time = time.strftime("%I:%M:%S %p")   # 12-hour format
    current_day  = time.strftime("%A")
    current_date = time.strftime("%d %B %Y")

    label_time.config(text=current_time)
    label_day.config(text=current_day)
    label_date.config(text=current_date)

    root.after(1000, update_clock)   # update every second


# Main window
root = tk.Tk()
root.title("Aesthetic Digital Clock")
root.geometry("500x300")
root.resizable(False, False)

# Background color
root.configure(bg="#0e0e0e")

# Time label
label_time = tk.Label(
    root,
    font=("Helvetica", 50, "bold"),
    fg="#00ffcc",
    bg="#0e0e0e"
)
label_time.pack(pady=20)

# Day label
label_day = tk.Label(
    root,
    font=("Helvetica", 20, "bold"),
    fg="#ffffff",
    bg="#0e0e0e"
)
label_day.pack()

# Date label
label_date = tk.Label(
    root,
    font=("Helvetica", 18),
    fg="#d9d9d9",
    bg="#0e0e0e"
)
label_date.pack(pady=10)

# Start the clock update loop
update_clock()

# Run the application
root.mainloop()
