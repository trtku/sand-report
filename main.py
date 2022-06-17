from src import csv_reader as reader
from src import csv_visualizer as vizualizer
from src import stress_strain as ss

if __name__=='__main__':
    smooth_factor = 10000
    filename = '20220616_test5.csv'

    csvfile = reader.read(filename)
    # csvfiles = reader.read_multi()
    vizualizer.viz(csvfile, smoothing=smooth_factor, prefix=filename, show=False, save=True)
    # vizualizer.viz_multi(csvfiles, smoothing=smooth_factor, show=True, save=False)
    ss.ssd(csvfile, smoothing=smooth_factor, prefix=filename, show=False, save=True)
    # ss.ssd_multi(csvfiles, smoothing=smooth_factor, show=False, save=True)
