import os
from analysis import *

folder = os.getcwd() + r'\Raman Data'
file = r'gold_baseline.txt'
fn = os.path.join(folder, file)
print(fn)
spectra = spline_WS2map_analysis(fn)
# print(list((spectra[0].keys())))
plot_map(spectra, 'D_height', show=True)
plot_hist(spectra, 'D_height', show=True)
