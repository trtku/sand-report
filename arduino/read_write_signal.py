import csv
import serial 
import datetime

i = 0  #カウント用
ser = serial.Serial("COM3")  # Arduinoが接続されているCOMポートを指定

while (i !=24): #24時間分計測＆保存(1時間×24回)
    
    #ファイル名の設定
    now = datetime.datetime.today()     #現在時刻取得       
    hourstr = "_" + now.strftime("%H")  #時刻を文字列化
    filename = "temphumid_" + now.strftime("%Y%m%d") + hourstr + ".csv"
    
    hourstr_ser = hourstr   #hourstr_serの初期化
    
    #csvファイルに書き込み
    with open(filename,'a',newline='') as f:  #csvファイルの生成
        writer = csv.writer(f)
        writer.writerow(["year","month","day","hour","minute","second","temp[℃]","humid[%]","heat index"])  #1行目：見出し
    
        while(hourstr == hourstr_ser):  #1時間データを書き込む
            
            #情報の取得
            temp = float(ser.readline().rstrip().decode(encoding='utf-8'))    #温度 
            humid = float(ser.readline().rstrip().decode(encoding='utf-8'))   #湿度
            hi = 0.8*temp +0.01*humid*(0.99*temp-14.3)+46.3;                  #不快指数
            now_ser = datetime.datetime.today()                               #現在時刻
            #[年，月，日，時，分，秒，温度，湿度，不快指数]
            data = [now_ser.year,now_ser.month,now_ser.day,now_ser.hour,
                         now_ser.minute,now_ser.second,temp,humid,hi] 
            
            hourstr_ser = "_" + now_ser.strftime("%H")  #時刻を文字列化
            
            #データの書き込み
            writer.writerow(data)  #1行目以降：データ
            
            #表示
            print('--------------------------------')
            print(now_ser.strftime("%Y/%m/%d %H:%M:%S"))
            print("温度：{:.2f}℃".format(temp))
            print("湿度：{:.2f}%".format(humid))
            print("不快指数：{:.2f}".format(hi))
            print("Wtite in {:}".format(filename))
    
    i+=1
    
ser.close()  #ポートを閉じる
print("End")