# smart_tracker/tracker_visualizer.py
import matplotlib.pyplot as plt
import pandas as pd

class Visualizer:
    def __init__(self):
        plt.style.use("ggplot")

    # ---------- Bar Chart ----------
    def plot_bar(self, df, col, title="Bar Chart"):
        if col not in df.columns:
            return

        counts = df[col].value_counts()

        plt.figure(figsize=(8, 5))
        plt.bar(counts.index.astype(str), counts.values)
        plt.title(title)
        plt.xlabel(col)
        plt.ylabel("Count")
        plt.tight_layout()
        plt.show()  
    # ---------- Line Chart ----------
    def plot_line(self, df, x_col, metric, title="Line Chart"):
        if x_col not in df.columns or metric not in df.columns:
            return
        
        df_sorted = df.sort_values(by=x_col)

        plt.figure(figsize=(8, 5))
        plt.plot(df_sorted[x_col], df_sorted[metric], marker='o')
        plt.title(title)
        plt.xlabel(x_col)
        plt.ylabel(metric)
        plt.tight_layout()
        plt.show()

    # ---------- Pie Chart ----------
    def plot_pie(self, df, col, title="Pie Chart"):
        if col not in df.columns:
            return

        counts = df[col].value_counts()

        plt.figure(figsize=(7, 7))
        plt.pie(counts, labels=counts.index, autopct='%1.1f%%')
        plt.title(title)
        plt.tight_layout()
        plt.show()
