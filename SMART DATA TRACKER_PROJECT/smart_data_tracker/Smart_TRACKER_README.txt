OOP PYTHON PROGRAMMING 

THE SMART DATA TRACKER : Python Tool for Monitoring and Visualizing Feild Data 
    By Nanfuka Fatuma 
    B36106

About the Application
    This is a light weight and offline tool built using Object -Oriented python to help users especially Monitoring and Evaluation practioners collect, manage , clean and visualize feild data in real time . 
    This is to mainly to provide a standardised tool as many M&E practionars perdominantly use Excel.

Key Features 
    1.Add /Edit / Delete records
    2.Save / Load CSV and SQlite
    3.Simple Visualization 3 optios , that is a Bar, Line and Pie chart
    4.Basic input validations
    Tkinter GUI

Requirements and running
    for this to be Run install Python 3.8+ form https://www.python.org/downloads/ then 
    pip install -r Requirements_libraries.txt
        clone repo
        "pip install -r Requirements_libraries.txt"
        enure the "sample_data.csv" exists in the same folder
        then run"Run_Smart_Tracker.py"

the folder should include ;
    Tracker / core modules of (records, dg_manager,visualizer,controller, GUI)
    "sample_data.csv"
    "Requirements_libraries.txt"
    and "this Smart_Tracker_README.txt"

    Below is the cshape 

                        smart-data-tracker/
                        │
                        ├── README.md
                        ├── Requirements_libraries.txt
                        ├── sample_data.csv
                        ├── smart_tracker/
                        │   ├── Tracker_records.py
                        │   ├── Trackerdb_manager.py
                        │   ├── Tracker_visualizer.py
                        │   ├── Tracker_controller.py
                        │   └── Tracker_GUI.py
                        └── Run_Smart_Tracker.py
