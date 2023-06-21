import pandas as pd
from os import listdir
import config


class Files:

    def __init__(self):
        self.dir_read = config.DIR_CSV
        self.dir_save = config.DIR_PROCESSED
        self.csv_headers = config.CSV_HEADERS

    def read(self):
        csv_name = listdir(self.dir_read)[0] if '.csv' in listdir(self.dir_read)[0] else TypeError
        csv_data = pd.read_csv(self.dir_read + '\\' + csv_name,
                               usecols=[0,1,2,3,8,10,17],
                               names=self.csv_headers)
        return csv_data, csv_name

    def save(self, dataframe, save_name):
        dataframe.to_csv(self.dir_save + '\\' + save_name, encoding='utf-8', index=False)
