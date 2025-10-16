import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime





class ClimexWeatherApp:
    def __init__(self,root):
        self.root = root
        self.root.title("ClimexWeatherApp")
        self.root.geometry("2000x600")
        self.root.resizable(False,False)

# Window setup
root = tk.Tk()
root.title("Climex Desktop App")
root.geometry("400x300")

# Add a label
label = tk.Label(root, text="Welcome to Climex!", font=("Arial", 16))
label.pack(pady=20)

# Add a button
def say_hello():
    messagebox.showinfo("Message", "Hello from Climex!")

button = tk.Button(root, text="Click Me", command=say_hello)
button.pack(pady=10)

# Run the app
root.mainloop()
