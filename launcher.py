import sys
import os

def start():
    # 1. Find the path to the 'app_source' folder
    if getattr(sys, 'frozen', False):
        # If running as compiled .exe
        base_path = os.path.dirname(sys.executable)
    else:
        # If running as script in VS Code
        base_path = os.path.dirname(os.path.abspath(__file__))
        
    source_path = os.path.join(base_path, 'app_source')

    # 2. Add it to Python's "search path" so we can import files from it
    if source_path not in sys.path:
        sys.path.insert(0, source_path)

    # 3. Import 'main' from that folder and run it
    try:
        import main 
        main.run_app()
    except ImportError as e:
        print(f"Error: Could not find app logic. {e}")
        input("Press Enter to exit...") # Keep window open to see error

if __name__ == "__main__":
    start()