from tkinter import *
from tkinter import filedialog
import pandas as pd


# function to open a window to select the file and to return the file path
def open_file():
    filepath = filedialog.askopenfilename()
    print(filepath)
    return filepath

# uses pandas to read the parquet file selected
parquet_file = open_file()
table_data = pd.read_parquet(parquet_file)

# print the data on console
# uses pandas query function to generate a percentile query
# shows data over 0.9 percentile trip distance
print(table_data.query('trip_distance > 0.9'))
print("Wait until the data is download to csv file")

# export data to csv file
query = table_data.query('trip_distance > 0.9')
query.to_csv('parquet_download.csv')
