import encodings
import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import math as m
import numpy as np

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



    def read_multi_csv(self, foldername, slice_csv=False, start=0, length=1):
        print('reading...')

        self.foldername = foldername
        self.folderpath = os.path.join(self.path_csv, foldername)
        self.csvfiles = []

        for file in os.listdir(self.folderpath):
            if file.endswith(".csv"):
                filepath = os.path.join(self.folderpath, file)

                csvfile = pd.read_csv(filepath, header=1, skiprows=[i+1 for i in range(18)], usecols=[0,1,2], names=['sec', 'N', 'mm'], encoding="shift-jis")
                self.csvfiles.append(csvfile)

        if slice_csv:
            self.csvfiles = self.csvfiles[start:start+length]


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


    def viz_multi_csv(self, smoothing=1000, show=False, save=False):

        plt.figure(figsize=(10,12), dpi=100)

        if len(self.csvfiles)==0:
            print('there is no csv file in this folder')
        elif len(self.csvfiles) == 1:
            plt.plot(self.csvfiles[0].rolling(smoothing).mean().mm, csvfile.rolling(smoothing).mean().N, label='test1', color='green')
        else:
            for i, csvfile in enumerate(self.csvfiles):
                color_index = "C" + str(i)
                plt.plot(csvfile.rolling(smoothing).mean().mm, csvfile.rolling(smoothing).mean().N, label='test'+str(i+1), color=color_index)

        plt.xlabel('delta, mm')
        plt.ylabel('compression force, N')
        plt.title('filename', fontdict={'fontsize':15,'fontweight':'bold'})
        plt.suptitle('1 axis compression test')
        plt.legend()

        if save:
            HERE = os.path.dirname(os.path.abspath(__file__))
            path_parent = os.path.dirname(HERE)
            path_data = os.path.join(path_parent, 'data')
            filename = os.path.join(path_data, 'std_multi.png')
            plt.savefig(filename)
        else:
            pass

        if show:
            plt.show()
        else:
            pass


    def ssd_multi(self, smoothing=1000, show=False, save=False):

        plt.figure(figsize=(10,12), dpi=100)

        #寸法入力
        L = 100.00 #mm #初期長さ
        D = 100.00 #diamter (mm)
        A = (D/2) * (D/2) * m.pi #mm**2 #断面積 

        for csvfile in self.csvfiles:

            #ひずみの計算
            # ε = dL / L
            csvfile['strain'] = csvfile.rolling(smoothing).mean().mm / L

            #0.2%耐力
            csvfile['strain_0.2%'] = csvfile['strain'] + 0.002
            #0.2%との交点の値
            # index = np.where(csvfile['strain'] == csvfile['strain_0.2%'])
            # print(index)

            #応力の計算
            # σ = F / A
            csvfile['stress(MPa)'] = (csvfile.rolling(smoothing).mean().N / A )

            #弾性域の範囲
            new = csvfile[(csvfile['strain'] > 0.015) & (csvfile['strain'] < 0.030)]
            # print(new)

            #傾きを求める
            x_1 = new['strain']
            y_1 = new['stress(MPa)']
            plt.scatter(x_1, y_1, s=6, c="black")
            plt.plot(x_1, np.poly1d(np.polyfit(x_1, y_1, 1))(x_1), label='d=1')
            a ,b= np.polyfit(x_1, y_1, 1)
            print("傾き　=　",a)
            print("切片　=　",b)

            #グラフを書く
            #0,1,2 = "sec","N","mm"
            # fig = plt.figure(figsize=(14, 10))
            x = csvfile['strain']
            y = csvfile['stress(MPa)']

            y2 = a*(x-0.002) + b

            #グラフ表示範囲
            # plt.xlim(0,1.2)
            # plt.ylim(0,600)

        #0.2%耐力直線
        # plt.scatter(x, y2, s=6, c="yellow") ##0.2%耐力要らない時はここを消す

        x2 = csvfile['strain_0.2%']
        plt.scatter(x, y, s=6, c="black")


        #交点の座標表示
        idx = np.argwhere(np.diff(np.sign(y - y2))).flatten()


        #交点の座標を書く
        i=0
        for i in idx.ravel(): #点が複数ある場合は、高い値を採用
            x[i] = round(x[i],3)
            y[i] = round(y[i],3)
        plt.text(x[i], y[i] ,'  ({x}, {y})'.format(x=x[i], y=y[i])) ##0.2%耐力要らない時はここを消す

        print('0.2%耐力',y[max(idx)])

        #引張強さ
        print('T.S = ' , y.max())


        #グラフの体裁
        # plt.tick_params(axis='both', direction='in',pad=10)
        plt.ylabel('Stress, σ/MPa')
        plt.xlabel('Strain, ε')
        plt.title('filename', fontdict={'fontsize':15,'fontweight':'bold'})
        plt.suptitle('stress-strain diagram')
        # plt.tick_params(labelsize=20)
        plt.legend()


        #グラフの表示
        if save:
            HERE = os.path.dirname(os.path.abspath(__file__))
            print(HERE)

            path_parent = os.path.dirname(HERE)
            print(path_parent)

            path_data = os.path.join(path_parent, 'data')
            filename = os.path.join(path_data, 'ssd_multi.png')
            plt.savefig(filename)
        else:
            pass
        
        if show:
            plt.show()
        else:
            pass


if __name__=='__main__':

    csv = csvManager()

    # csv.read_csv(foldername='compression_test', filename='20220524_test1.csv')
    # csv.read_csv(foldername='co2_monitoring', filename='co2_injection.csv')
    # csv.viz_csv()


    csv.read_multi_csv(foldername='compression_test', slice_csv=True, start=13, length=4)
    csv.viz_multi_csv(smoothing=1000, show=True, save=False)
    csv.ssd_multi(smoothing=1000, show=True, save=False)

    
