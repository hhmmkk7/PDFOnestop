import tkinter as tk
# Notice we can just import other files from the same folder!
import gui
import pdf_ops 

def run_app():
    root = tk.Tk()
    root.title("PDF OneStop")
    root.geometry("400x300")
    
    # Pass the 'root' to the GUI module to draw buttons
    gui.setup_ui(root)
    
    root.mainloop()