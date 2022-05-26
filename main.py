from src import csv_reader as reader
from src import csv_visualizer as vizualizer
from src import stress_strain as ss

if __name__=='__main__':
    smooth_factor = 10000

    csvfile = reader.read(filename='20220524_test5.csv')
    # csvfiles = reader.read_multi()
    vizualizer.viz(csvfile, smoothing=smooth_factor, show=False, save=True)
    # vizualizer.viz_multi(csvfiles, smoothing=smooth_factor, show=False, save=True)
    ss.ssd(csvfile, smoothing=smooth_factor, show=False, save=True)
    # ss.ssd_multi(csvfiles, smoothing=smooth_factor, show=False, save=True)
