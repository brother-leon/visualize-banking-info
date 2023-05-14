import csv
from os import listdir
import config


class Files:

    def __init__(self):
        self.dir_read = config.DIR_CSV
        self.dir_save = config.DIR_PROCESSED

    def read(self):
        csv_name = listdir(self.dir_read)[0] if '.csv' in listdir(self.dir_read)[0] else TypeError
        csv_data = csv.reader(csv_name, delimiter=',')
        line_count = 0
        for file_line, _ in enumerate(csv_data):
            line_count += 1
        print('Opened: ' + csv_name + f' contains {line_count} transactions.')
        return csv_data

    def save(self):
        pass

files = Files()
files.read()
