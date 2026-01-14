import sys
import os

def start_engine():
    # 1. Determine the root path (works for both .exe and script)
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    # 2. Find the source code folder
    source_dir = os.path.join(base_path, 'app_source')

    # 3. Add to Python path so we can import from it
    if source_dir not in sys.path:
        sys.path.insert(0, source_dir)

    # 4. Launch the App
    try:
        import main
        main.start_app()
    except ImportError as e:
        import tkinter.messagebox
        tkinter.messagebox.showerror("Critical Error", f"Could not load app_source.\n{e}")
    except Exception as e:
        import tkinter.messagebox
        tkinter.messagebox.showerror("Crash", f"An unexpected error occurred:\n{e}")

if __name__ == "__main__":
    start_engine()