# run_tracker.py
import tkinter as tk
from Tracker_GUI import TrackerGUI
def main():
    root = tk.Tk()
    app = TrackerGUI(root, csv_path="sample_data.csv")
    root.mainloop()
if __name__ == "__main__":
    main()  