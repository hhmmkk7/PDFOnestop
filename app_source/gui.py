import tkinter as tk
from tkinter import messagebox

def build_interface(root):
    # A simple label
    lbl = tk.Label(root, text="Hi! This is the demo.", font=("Helvetica", 16))
    lbl.pack(pady=40, padx=20)

    # A button to prove logic works
    btn = tk.Button(root, text="Click Me", command=say_hello)
    btn.pack(pady=10)

def say_hello():
    messagebox.showinfo("Hello", "The multi-file setup is working perfectly!")