import tkinter as tk
import gui  # We can import this because they are in the same folder

def start_app():
    # 1. Setup the main window
    root = tk.Tk()
    root.title("My Demo App")
    root.geometry("400x250")

    # 2. Hand over control to the GUI module
    gui.build_interface(root)

    # 3. Start the loop
    root.mainloop()