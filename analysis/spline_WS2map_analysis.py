from .imports import *
from .figure_generation import *
def spline_WS2map_analysis(fn,gen_figures=True):
    '''
    :param fn: name of file containing map
    :return:  a spectra that has a full analysis, saving the file as a .p format in the same location
    '''
    spectra = import_raman_map(fn)
    print('Map running - spline_WS2map_analysis Version')
    if 'fitted_spectrum' not in spectra[0]:
        spectra = get_WS2_fit_spline(spectra, 'data')
        print('peaks get_WS2_fit_carbon_maps fitted')
    save_data(spectra,fn)
    print('data saved')

    print('generating figures...')
    generate_figures(spectra,fn);

    return  spectra
