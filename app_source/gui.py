import tkinter as tk
from tkinter import messagebox
import pdf_ops  # We can import logic here too

def setup_ui(root):
    label = tk.Label(root, text="PDF OneStop Tool", font=("Arial", 16))
    label.pack(pady=20)

    btn = tk.Button(root, text="Check PDF Version", command=lambda: check_pdf())
    btn.pack(pady=10)

def check_pdf():
    # Call the logic from the other file
    result = pdf_ops.get_pdf_info("dummy.pdf") 
    messagebox.showinfo("Result", result)