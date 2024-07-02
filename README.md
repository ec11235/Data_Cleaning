CSV Data Cleaner

This project provides a comprehensive tool to clean and preprocess a CSV datasets. 
It enables users to handle missing values, change data types, and remove duplicates efficiently. 
The cleaned data can be displayed in a web browser for easy inspection.

Features
Display missing values and data types of the dataset.
Replace or remove rows with missing values.
Change the data types of columns.
Generate HTML views of the dataset for easy inspection.
Interactive command-line interface for user input.

Prerequisites
Python 
Pandas
Webbrowser
OS module

Usage:
- place your dataset into the data directory
- update the filepath in preprocessing.py to match your CSV (line 5: FILE_PATH = "data/netflix_data.csv")
- run preprocessing.py (python preprocessing.py)

Current netflix dataset taken from Kaggle: https://www.kaggle.com/datasets/shivamb/netflix-shows