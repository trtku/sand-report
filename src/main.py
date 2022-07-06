# from src import csv_reader as reader
# from src import csv_visualizer as vizualizer
from csv_manager import csv_to_ssd as ss
from csv_manager import csvManager

if __name__=='__main__':
    smooth_factor = 10000
    filename = '20220616_test5.csv'

    # csvfile = reader.read(filename)    
    # vizualizer.viz(csvfile, smoothing=smooth_factor, prefix=filename, show=False, save=True)
    # ss.ssd(csvfile, smoothing=smooth_factor, prefix=filename, show=False, save=True)
    
    # csvfiles = reader.read_multi()
    # vizualizer.viz_multi(csvfiles, smoothing=smooth_factor, show=False, save=True)
    # ss.ssd_multi(csvfiles, smoothing=smooth_factor, show=False, save=True)

    csv = csvManager()

    # read(foldername='compression_test', filename='20220524_test1.csv)
    csv.read_csv(foldername='co2_monitoring', filename='co2_injection.csv')
    # csv.read_csv(foldername='co2_monitoring', filename='co2_ordinary_day.csv')

    csv.viz_csv()