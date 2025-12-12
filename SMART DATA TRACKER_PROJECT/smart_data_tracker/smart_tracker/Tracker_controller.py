# smart_tracker/controller.py
from Trackerdb_manager import DatabaseManager
from Tracker_records import Record
import pandas as pd

class AppController:
    def __init__(self, csv_path="sample_data.csv"):
        self.db = DatabaseManager(csv_path=csv_path)
        # ensure sqlite created
        try:
            df = self.db.load_csv()
            self.db.to_sqlite(df)
        except Exception:
            # if file missing, create empty structure
            df = pd.DataFrame(columns=['ID','SEX','AGE','MARTAL','EDUC','WEIGHT','HIEGHT',
                                       'HALTH_RATE','FILTRATE','SMOKE','ALCOHOLE','CAFFIENE',
                                       'HOURWRINT','HOURWEND','HOURNEED','TROUBLESLEEP',
                                       'ANXIETY','DPRESSION','STAYLEPRC','GETSLEPREC']) 
            
            df.to_csv(csv_path, index=False)
            self.db.to_sqlite(df)

    def list_records(self):
        return self.db.load_csv()

    def add(self, row_dict):
        # validate
        ok, errors = Record.validate(row_dict)
        if not ok:
            return False, errors
        rec = Record(**{k: row_dict[k] for k in ["ID","SEX","AGE","MARTAL","EDUC","WEIGHT","HIEGHT",
                                               "HALTH_RATE","FILTRATE","SMOKE","ALCOHOLE","CAFFIENE",
                                               "HOURWRINT","HOURWEND","HOURNEED","TROUBLESLEEP",
                                               "ANXIETY","DPRESSION","STAYLEPRC","GETSLEPREC"]})
        
        self.db.append_record(rec)
        return True, None
    
    def delete(self, rec_id):
        return self.db.delete_by_id(rec_id)

    def update(self, rec_id, updates):
        return self.db.update_record(rec_id, updates)

    def search(self, **kwargs):
        return self.db.search(**kwargs)
