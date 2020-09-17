import csv
import os

from ErrDecorator import log_errors, NotNameError, NotEmailError


class FileManager:
    """
    gets a directory
    if the file ends with 'csv'
    the generator gives the found files for processing
    """
    def __init__(self, src):
        self.src = src

    def get_files(self):
        for dirpath, dirnames, filenames in os.walk(self.src):
            for file in filenames:
                if file.endswith('csv'):
                    yield os.path.join(dirpath, file)


class FilterCSV:
    """
    reads FileManager data
    and checks the row in the file
    if the row is invalid
    then this is reported
    and the function 'check_line' is wrapped in a decorator 'log_errors'
    which writes to the file err_data_csv.log
    """
    def __init__(self, src):
        self.src = os.path.normpath(src)

    def csv_reader(self):
        for files in FileManager(src=self.src).get_files():
            with open(files, "r") as f_obj:
                reader = csv.reader(f_obj)
                for index_row, row in enumerate(reader):
                    if index_row == 0:
                        continue
                    try:
                        self.check_line(row)
                    except (NotNameError, NotEmailError, ValueError) as exc:
                        print(f'Invalid format: {exc} in {files} line {index_row + 1}')

    @log_errors('err_data_csv.log')
    def check_line(self, line):
        name, email, data = line
        if not name.isalnum():
            raise NotNameError
        if '@' not in email or '.' not in email:
            raise NotEmailError
