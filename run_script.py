import argparse
import csv_filter

parser = argparse.ArgumentParser(description='CSV filter')
parser.add_argument('-p', '--path', type=str, metavar='', help='directory path')
args = parser.parse_args()

if __name__ == '__main__':
    try:
        filter_csv = csv_filter.FilterCSV(src=args.path)
        filter_csv.csv_reader()
    except FileNotFoundError as exc:
        print(f"Error: {exc} type {(type(exc))}")
