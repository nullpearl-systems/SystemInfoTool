import tkinter as tk
import wmi
import winsound
import sys
import os

# Resolve path for the audio file
def resource_path(relative_path):
    """Get the absolute path to the resource."""
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Path to the custom audio file
audio_file = resource_path("system-standby.wav")

# Play the custom audio when the application starts
winsound.PlaySound(audio_file, winsound.SND_FILENAME)

# Initialize the WMI client
c = wmi.WMI()

# Gather system information
manufacturer = c.Win32_ComputerSystem()[0].Manufacturer
model = c.Win32_ComputerSystem()[0].Model
processor = c.Win32_Processor()[0].Name
ram = round(int(c.Win32_ComputerSystem()[0].TotalPhysicalMemory) / (1024 ** 3), 2)

# Create the main window
root = tk.Tk()
root.title("Yo! System Check")
root.geometry("600x350")
root.config(bg="#f7f7f7")

# UI Components
title_label = tk.Label(root, text="Check Check System Check!", font=("Arial", 16, "bold"), fg="#2C3E50", bg="#f7f7f7")
title_label.pack(pady=10)

info_frame = tk.Frame(root, bg="#ffffff", padx=20, pady=15)
info_frame.pack(padx=20, pady=20, fill="both", expand=True)

labels = [
    ("System Manufacturer: ", manufacturer),
    ("System Model: ", model),
    ("Processor: ", processor),
    ("Total RAM: ", f"{ram} GB"),
]

for i, (label_text, value_text) in enumerate(labels):
    label = tk.Label(info_frame, text=label_text, font=("Arial", 12, "bold"), fg="#34495E", bg="#ffffff")
    value = tk.Label(info_frame, text=value_text, font=("Arial", 10), fg="#2C3E50", bg="#ffffff")
    label.grid(row=i, column=0, sticky="w", padx=(0, 10), pady=5)
    value.grid(row=i, column=1, sticky="w", pady=5)

def close_window():
    root.destroy()

close_button = tk.Button(root, text="Close", command=close_window, font=("Arial", 10), bg="#3498DB", fg="white", relief="flat", width=20, height=2)
close_button.pack(pady=20)

close_button.bind("<Enter>", lambda event: close_button.config(bg="#2980B9"))
close_button.bind("<Leave>", lambda event: close_button.config(bg="#3498DB"))

# Run the application
root.mainloop()
