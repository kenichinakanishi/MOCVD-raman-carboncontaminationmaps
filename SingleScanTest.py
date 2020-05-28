import os
from analysis import *

folder = os.getcwd() + r'\Raman Data'
file = r'dms0_05mbar_singlescan.txt'
fn = os.path.join(folder, file)
spectra = spline_WS2_analysis_carbon(fn)
# print(spectra)
print('done')

plot_samples_spline(spectra, 'fitted_spectrum', 'data', no_samples=1)

# print(spectra[0]['D_height'])
# print(list((spectra[0].keys())))
