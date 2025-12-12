# smart_tracker/tracker_records.py
from dataclasses import dataclass, asdict
from datetime import datetime

class Record:
    def __init__(self, ID, SEX, AGE, MARTAL, EDUC, WEIGHT, HIEGHT, HALTH_RATE,
                 FILTRATE, SMOKE, ALCOHOLE, CAFFIENE, HOURWRINT, HOURWEND,
                 HOURNEED, TROUBLESLEEP, ANXIETY, DPRESSION, STAYLEPRC,
                 GETSLEPREC):

        self.ID = ID
        self.SEX = SEX
        self.AGE = AGE
        self.MARTAL = MARTAL
        self.EDUC = EDUC
        self.WEIGHT = WEIGHT
        self.HIEGHT = HIEGHT
        self.HALTH_RATE = HALTH_RATE
        self.FILTRATE = FILTRATE
        self.SMOKE = SMOKE
        self.ALCOHOLE = ALCOHOLE
        self.CAFFIENE = CAFFIENE
        self.HOURWRINT = HOURWRINT
        self.HOURWEND = HOURWEND
        self.HOURNEED = HOURNEED
        self.TROUBLESLEEP = TROUBLESLEEP
        self.ANXIETY = ANXIETY
        self.DPRESSION = DPRESSION
        self.STAYLEPRC = STAYLEPRC
        self.GETSLEPREC = GETSLEPREC

    def to_dict(self):
        return {
            "ID": self.ID,
            "SEX": self.SEX,
            "AGE": self.AGE,
            "MARTAL": self.MARTAL,
            "EDUC": self.EDUC,
            "WEIGHT": self.WEIGHT,
            "HIEGHT": self.HIEGHT,
            "HALTH_RATE": self.HALTH_RATE,
            "FILTRATE": self.FILTRATE,
            "SMOKE": self.SMOKE,
            "ALCOHOLE": self.ALCOHOLE,
            "CAFFIENE": self.CAFFIENE,
            "HOURWRINT": self.HOURWRINT,
            "HOURWEND": self.HOURWEND,
            "HOURNEED": self.HOURNEED,
            "TROUBLESLEEP": self.TROUBLESLEEP,
            "ANXIETY": self.ANXIETY,
            "DPRESSION": self.DPRESSION,
            "STAYLEPRC": self.STAYLEPRC,
            "GETSLEPREC": self.GETSLEPREC
        }
    @staticmethod
    def validate(data: dict):
        errors = []
        required_fields = ["ID", "SEX", "AGE", "MARTAL", "EDUC", "WEIGHT", "HIEGHT",
                           "HALTH_RATE", "FILTRATE", "SMOKE", "ALCOHOLE", "CAFFIENE",
                           "HOURWRINT", "HOURWEND", "HOURNEED", "TROUBLESLEEP",
                           "ANXIETY", "DPRESSION", "STAYLEPRC", "GETSLEPREC"]   
        for field in required_fields:
            if field not in data:
                errors.append(f"Missing field: {field}")
        if errors:
            return False, errors
        return True, []
    
    