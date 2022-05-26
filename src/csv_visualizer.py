import matplotlib.pyplot as plt
import os



def viz(csvfile, smoothing=1000, show=False, save=False):

    plt.figure(figsize=(10,12), dpi=100)

    plt.plot(csvfile.rolling(smoothing).mean().sec, csvfile.rolling(smoothing).mean().N, label='test1', color='green')

    plt.xlabel('time, sec')
    plt.ylabel('compression force, N')
    plt.title('filename', fontdict={'fontsize':15,'fontweight':'bold'})
    plt.suptitle('1 axis compression test')
    plt.legend()

    if save:
        HERE = os.path.dirname(os.path.abspath(__file__))
        path_parent = os.path.dirname(HERE)
        path_data = os.path.join(path_parent, 'data')
        filename = os.path.join(path_data, 'std.png')
        plt.savefig(filename)
    else:
        pass

    if show:
        plt.show()
    else:
        pass

def viz_multi(csvfiles, smoothing=1000, show=False, save=False):

    plt.figure(figsize=(10,12), dpi=100)

    if len(csvfiles)==0:
        print('there is no csv file in this folder')
    elif len(csvfiles) == 1:
        plt.plot(csvfiles[0].rolling(smoothing).mean().sec, csvfile.rolling(smoothing).mean().N, label='test1', color='green')
    else:
        for i, csvfile in enumerate(csvfiles):
            color_index = "C" + str(i)
            plt.plot(csvfile.rolling(smoothing).mean().sec, csvfile.rolling(smoothing).mean().N, label='test'+str(i+1), color=color_index)

    plt.xlabel('time, sec')
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

if __name__=='__main__':
    # p1=csvfile1['N'].max()
    pass
