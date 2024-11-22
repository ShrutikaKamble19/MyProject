import tkinter as tk
from time import strftime

def update_time():
    """
    Updates the label with the current time and schedules the next update.
    """
    current_time = strftime("%H:%M:%S %p")  # Format: Hour:Minute:Second AM/PM
    time_label.config(text=current_time)
    time_label.after(1000, update_time)  # Update every 1000ms (1 second)

# Initialize the main window
root = tk.Tk()
root.title("Digital Clock")

# Create a label to display the time
time_label = tk.Label(root, font=("Helvetica", 48), background="black", foreground="cyan")
time_label.pack(anchor="center")

# Start the clock by calling the update_time function
update_time()

# Run the main event loop
root.mainloop()