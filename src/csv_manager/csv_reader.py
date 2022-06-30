import os
import pandas as pd


HERE = os.path.dirname(os.path.abspath(__file__))
path_parent = os.path.dirname(HERE)
path_data = os.path.join(path_parent, 'data')


def read(filename='20220524_test1.csv'):
    print('reading...')

    filepath = os.path.join(path_data, filename)

    csvfile = pd.read_csv(filepath, header=1, skiprows=[i+1 for i in range(18)], usecols=[0,1,2], names=['sec', 'N', 'mm'], encoding="shift-jis")

    return csvfile

def read_multi(foldername=path_data):
    print('reading...')

    csvfiles = []

    for file in os.listdir(foldername):
        if file.endswith(".csv"):
            filepath = os.path.join(foldername, file)

            csvfile = pd.read_csv(filepath, header=1, skiprows=[i+1 for i in range(18)], usecols=[0,1,2], names=['sec', 'N', 'mm'], encoding="shift-jis")
            csvfiles.append(csvfile)
    return csvfiles

if __name__=='__main__':
    read_multi()