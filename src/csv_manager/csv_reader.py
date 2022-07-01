import encodings
import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

class csvManager(object):
    def __init__(self):
        # get necessary path
        self.path_csv_manager = os.path.dirname(os.path.abspath(__file__))
        self.path_src = os.path.dirname(os.path.abspath(self.path_csv_manager))
        self.path_sand_report = os.path.dirname(os.path.abspath(self.path_src))
        self.path_data = os.path.join(self.path_sand_report, 'data')
        self.path_csv = os.path.join(self.path_data, 'csv')
        self.path_png = os.path.join(self.path_data, 'png')


    def read_csv(self, foldername, filename):

        self.foldername = foldername
        self.filename = filename

        self.filepath = os.path.join(self.path_csv, foldername, filename)

        if foldername=='compression_test':
            self.csvfile = pd.read_csv(self.filepath, header=1, skiprows=[i+1 for i in range(18)], usecols=[0,1,2], names=['sec', 'N', 'mm'], encoding="shift-jis")
        elif foldername=='co2_monitoring':
            self.csvfile = pd.read_csv(self.filepath, index_col=0, names=['ind', 'ppm', 'degree', '%'])
        else:
            raise Exception ("csvfile cannot read from the specified folder")



    def read_multi_csv(self, foldername):
        print('reading...')

        csvfiles = []

        for file in os.listdir(foldername):
            if file.endswith(".csv"):
                filepath = os.path.join(foldername, file)

                csvfile = pd.read_csv(filepath, header=1, skiprows=[i+1 for i in range(18)], usecols=[0,1,2], names=['sec', 'N', 'mm'], encoding="shift-jis")
                csvfiles.append(csvfile)
        return csvfiles


    def viz_csv(self, smoothing=0, prefix='prefix', show=True, save=False):

        plt.figure(figsize=(10,12), dpi=100)

        if self.foldername=='compression_test':
            plt.plot(self.csvfile.rolling(smoothing).mean().sec, self.csvfile.rolling(smoothing).mean().N, label='test1', color='green')
            plt.xlabel('time, sec')
            plt.ylabel('compression force, N')
            plt.title('filename', fontdict={'fontsize':15,'fontweight':'bold'})
            plt.suptitle('1 axis compression test')

        elif self.foldername=='co2_monitoring':
            # self.csvfile['datetime'] = self.csvfile['datetime'].map(lambda x: datetime.strptime(str(x), '%y-%m-%d %H:%M:%S.%f'))
            # x = self.csvfile['datetime']
            y = self.csvfile['ppm']
            y.plot(title = 'test')
            # plt.plot(x, y)
            # plt.xlabel('time, sec')
            # plt.ylabel('co2 density, ppm')
            # plt.title('filename', fontdict={'fontsize':15,'fontweight':'bold'})
            # plt.suptitle('co2 monitoring')
        
        plt.legend()

        if show:
            plt.show()

        if save:
            filename = os.path.join(self.path_png, 'test_{}.png'.format(prefix))
            plt.savefig(filename)


if __name__=='__main__':

    csv = csvManager()

    # read(foldername='compression_test', filename='20220524_test1.csv)
    csv.read_csv(foldername='co2_monitoring', filename='co2_injection.csv')
    # csv.read_csv(foldername='co2_monitoring', filename='co2_ordinary_day.csv')

    csv.viz_csv()
    
