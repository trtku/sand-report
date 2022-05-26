
import numpy as np
import matplotlib.pyplot as plt
import math as m
import os

def ssd(csvfile, smoothing=1000, show=False, save=False):

    plt.figure(figsize=(10,12), dpi=100)

    #寸法入力
    L = 140.00 #mm #初期長さ
    D = 80.00 #diamter (mm)
    A = (D/2) * (D/2) * m.pi #mm**2 #断面積 

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
    new = csvfile[(csvfile['strain'] > 0.000) & (csvfile['strain'] < 0.0125)]
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
    plt.scatter(x, y2, s=6, c="yellow") ##0.2%耐力要らない時はここを消す

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
        filename = os.path.join(path_data, 'ssd.png')
        plt.savefig(filename)
    else:
        pass

    if show:
        plt.show()
    else:
        pass



def ssd_multi(csvfiles, smoothing=1000, show=False, save=False):

    plt.figure(figsize=(10,12), dpi=100)

    #寸法入力
    L = 140.00 #mm #初期長さ
    D = 80.00 #diamter (mm)
    A = (D/2) * (D/2) * m.pi #mm**2 #断面積 

    for csvfile in csvfiles:

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
        new = csvfile[(csvfile['strain'] > 0.0005) & (csvfile['strain'] < 0.015)]
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
    plt.scatter(x, y2, s=6, c="yellow") ##0.2%耐力要らない時はここを消す

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
        filename = os.path.join(path_data, 'ssd.png')
        plt.savefig(filename)
    else:
        pass
    
    if show:
        plt.show()
    else:
        pass
