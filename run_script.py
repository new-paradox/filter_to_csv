from sys import argv
import csv_filter

script_name, src = argv
try:
    filter_csv = csv_filter.FilterCSV(src)
    filter_csv.csv_reader()
except FileNotFoundError as exc:
    print("Don't worry, the path may be incorrectly entered")
