# Tracker_GUI.py
# smart_tracker/tracker_gui.py
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from Tracker_controller import AppController
from Tracker_visualizer import Visualizer
import pandas as pd

class TrackerGUI:
    def __init__(self, master, csv_path="sample_data.csv"):
        self.master = master
        self.master.title("Smart Data Tracker - Nanfuka Fatuma-B36106")
        self.controller = AppController(csv_path=csv_path)
        self.visualizer = Visualizer()
        self.build_ui()
        self.refresh_table()
        

    def build_ui(self):
        self.root = self.master
        self.db = self.controller.db
        self.fields = [
            "ID","SEX","AGE","MARTAL","EDUC","WEIGHT","HIEGHT",
            "HALTH_RATE","FILTRATE","SMOKE","ALCOHOLE","CAFFIENE",
            "HOURWRINT","HOURWEND","HOURNEED","TROUBLESLEEP",
            "ANXIETY","DPRESSION","STAYLEPRC","GETSLEPREC"
        ]
        frm = ttk.Frame(self.root)
        frm.pack(fill='both', expand=True)

        # Form inputs
        f1 = ttk.LabelFrame(frm, text="Add / Update Record")
        f1.pack(fill='x', padx=5, pady=5)

        labels = ["ID","SEX","AGE","MARTAL","EDUC","WEIGHT","HIEGHT",
                  "HALTH_RATE","FILTRATE","SMOKE","ALCOHOLE","CAFFIENE",
                  "HOURWRINT","HOURWEND","HOURNEED","TROUBLESLEEP",
                  "ANXIETY","DPRESSION","STAYLEPRC","GETSLEPREC"]
        self.entries = {}
        for i, l in enumerate(labels):
            ttk.Label(f1, text=l.capitalize()).grid(row=i//4, column=(i%4)*2, sticky='w', padx=3, pady=3)
            ent = ttk.Entry(f1, width=18)
            ent.grid(row=i//4, column=(i%4)*2+1, padx=3, pady=3)
            self.entries[l] = ent

        ttk.Button(f1, text="Add Record", command=self.add_record).grid(row=5, column=0, padx=3, pady=5)
        ttk.Button(f1, text="Delete Record", command=self.delete_record).grid(row=5, column=1, padx=3, pady=5)
        ttk.Button(f1, text="Import CSV", command=self.import_csv).grid(row=5, column=2, padx=3, pady=5)
        ttk.Button(f1, text="Export CSV", command=self.export_csv).grid(row=5, column=3, padx=3, pady=5)

        # Table
        f2 = ttk.LabelFrame(frm, text="Records")
        f2.pack(fill='both', expand=True, padx=5, pady=5)
        cols = ["ID","SEX","AGE","MARTAL","EDUC","WEIGHT","HIEGHT","HALTH_RATE","FILTRATE","SMOKE","ALCOHOLE","CAFFIENE","HOURWRINT","HOURWEND","HOURNEED","TROUBLESLEEP","ANXIETY","DPRESSION","STAYLEPRC","GETSLEPREC"]  
        self.tree = ttk.Treeview(f2, columns=cols, show='headings')
        for c in cols:
            self.tree.heading(c, text=c)
            self.tree.column(c, width=100, anchor='center') 
        self.tree.pack(fill='both', expand=True)
        scrollbar = ttk.Scrollbar(f2, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side='right', fill='y')

        # Visualization
        f3 = ttk.Frame(frm)
        f3.pack(fill='x', padx=5, pady=5)
        ttk.Button(f3, text="Plot Bar Chart", command=self.plot_bar).pack(side='left', padx=5)
        ttk.Button(f3, text="Plot Line Chart", command=self.plot_line).pack(side='left', padx=5)
        ttk.Button(f3, text="Plot Pie Chart", command=self.plot_pie).pack(side='left', padx=5)


    def refresh_table(self):
        for r in self.tree.get_children():
            self.tree.delete(r)
        df = self.controller.list_records()
        for _, row in df.iterrows():
            self.tree.insert('', 'end', values=list(row))

    def add_record(self):
        row_dict = {k: self.entries[k].get().strip() for k in self.entries}
        ok, errors = self.controller.add(row_dict)
        if not ok:
            messagebox.showerror("Validation Error", "\n".join(errors))
            return
        messagebox.showinfo("Success", "Record added successfully.")
        self.refresh_table()
        
    def delete_record(self):
        rec_id = self.entries["ID"].get().strip()
        if not rec_id:
            messagebox.showerror("Error", "Please enter an ID to delete.")
            return
        self.controller.delete(rec_id)
        messagebox.showinfo("Deleted", f"Record with ID {rec_id} deleted.")
        self.refresh_table()    
        
    def import_csv(self):
        path = filedialog.askopenfilename(filetypes=[("CSV files","*.csv")])
        if path:
            df = pd.read_csv(path)
            self.controller.db.save_csv(df, out_path="sample_data.csv")
            self.controller.db.to_sqlite(df)
            messagebox.showinfo("Imported", "CSV imported to sample_data.csv")
            self.refresh_table()

    def export_csv(self):
        path = filedialog.asksaveasfilename(defaultextension=".csv")
        df = self.controller.list_records()
        df.to_csv(path, index=False)
        messagebox.showinfo("Exported", f"Saved to {path}")

    def plot_bar(self):
        df = self.controller.list_records()
        self.visualizer.plot_bar(df, col='SEX', title="Gender Distribution")
    
    def plot_line(self):
        df = self.controller.list_records()
        self.visualizer.plot_line(df, x_col='AGE', metric='HOURNEED', title="Sleep Hours Needed by Age")

    def plot_pie(self):
        df = self.controller.list_records()
        self.visualizer.plot_pie(df, col='SMOKE',title="Smoking Status Distribution")