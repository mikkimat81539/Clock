import time
from datetime import datetime
import tkinter as tk

screen = tk.Tk()
screen.geometry("500x150")
screen.title("Digital Clock")


time = tk.Label(screen, text=time.strftime("%a, %b %d,%Y %H:%M%p"), font=("Courier", 30), foreground="#21fff0")
time.pack(pady=50)

def update_time():
    # Get the current time
    current_time = datetime.now()

    formatted_time = current_time.strftime("%a, %b %d, %Y %I:%M %p")  # 12-hour format with AM/PM

    # Update the label with the current time
    time.config(text=formatted_time)

    # Check if the current time matches 6:00 (AM or PM)
    if 6 <= current_time.hour < 18:
        time.config(foreground="blue", background="white")
        screen.configure(background='white')

    else:
        time.config(foreground="#21fff0")

update_time()

screen.mainloop()
