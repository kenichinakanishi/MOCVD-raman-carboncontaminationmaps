import os
from analysis import *

folder = os.getcwd() + r'\Raman Data'
file = r'dms0_3mbar_map.txt'
fn = os.path.join(folder, file)
print(fn)
spectra = spline_WS2map_analysis(fn)
# print(list((spectra[0].keys())))
plot_map(spectra, 'WS1_height', show=True)
plot_hist(spectra, 'G_height', show=True)

data = []
data_point = spectra[100]
data.append(data_point)
plot_samples_spline(data, 'fitted_spectrum', 'data', no_samples=1)