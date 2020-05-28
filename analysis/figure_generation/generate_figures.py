from analysis.plotting import *
def generate_figures(spectra,fn, statistics=True):
    import os
    import matplotlib.pyplot as plt
    fn = fn[:-4];
    if not os.path.exists(fn):
        os.makedirs(fn);

    listoffigs = [
        'WS1_height',
        'WS2_height',
        'D_height',
        'G_height',
        'WS1_area',
        'WS2_area',
        'D_area',
        'G_area'
    ];
    for key in listoffigs:
        try:
            plot = plot_hist(spectra, key, statistics,show=False);
            plt.savefig(os.path.join(fn,'Histogram of ' + key));
        except Exception as e: print(e)
        #except:
            #print('Error saving Histograms')
            #pass
        plt.cla();
        plt.clf();
        try:
            plot = plot_map(spectra,key,show=False);
            plt.savefig(os.path.join(fn,'Map of ' + key));
        except:
            print('Error saving Plots');
            pass
        plt.cla();
        plt.clf();
