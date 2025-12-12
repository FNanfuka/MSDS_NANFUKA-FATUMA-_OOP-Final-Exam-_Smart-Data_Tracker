# smart_tracker/trackerdb_manager.py
import pandas as pd
import sqlite3
import os
import csv
import pathlib  
from pathlib import Path
from Tracker_records import Record

class DatabaseManager:
    def __init__(self, csv_path="sample_data.csv"):
        self.csv_path = csv_path

        if not os.path.exists(self.csv_path):
            df = pd.DataFrame(columns=[
                "ID","SEX","AGE","MARTAL","EDUC","WEIGHT","HIEGHT",
                "HALTH_RATE","FILTRATE","SMOKE","ALCOHOLE","CAFFIENE",
                "HOURWRINT","HOURWEND","HOURNEED","TROUBLESLEEP",
                "ANXIETY","DPRESSION","STAYLEPRC","GETSLEPREC"
            ])
            df.to_csv(self.csv_path, index=False)

    def load_data(self):
        return pd.read_csv(self.csv_path)

    def save_data(self, df):
        df.to_csv(self.csv_path, index=False)

    def add_record(self, record_dict):
        df = self.load_data()
        df = pd.concat([df, pd.DataFrame([record_dict])], ignore_index=True)
        self.save_data(df)

    def delete_record(self, record_id):
        df = self.load_data()
        df = df[df["ID"] != record_id]
        self.save_data(df)

    def update_record(self, record_id, new_data):
        df = self.load_data()
        df.loc[df["ID"] == record_id, new_data.keys()] = new_data.values()
        self.save_data(df)
    def to_sqlite(self, df, db_path="tracker_data.db", table_name="records"):
        conn = sqlite3.connect(db_path)
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        conn.close()    
    def load_csv(self):
        return pd.read_csv(self.csv_path)
    def save_csv(self, df, out_path="sample_data.csv"):
        df.to_csv(out_path, index=False)
    def append_record(self, record: Record):
        df = self.load_csv()
        df = pd.concat([df, pd.DataFrame([record.to_dict()])], ignore_index=True)
        self.save_csv(df)
    def delete_by_id(self, rec_id):
        df = self.load_csv()
        df = df[df["ID"] != rec_id]
        self.save_csv(df)
    def update_record(self, rec_id, updates: dict):
        df = self.load_csv()
        df.loc[df["ID"] == rec_id, updates.keys()] = updates.values()
        self.save_csv(df)
    def search(self, **kwargs):
        df = self.load_csv()
        for k, v in kwargs.items():
            df = df[df[k] == v]
        return df