from analysis.imports import *
from analysis.spline_fits import *

def create_entry(spectra,entry_name,key1,key2,function):
    '''
    :param spectra: the dictionary of spectrum and metadata
    :param entry_name: the name of the entry to be changed
    :param key1: the name of the first variable
    :param key2: the name of the second variable
    :param function: a function of 2 variables that give a single numeric output
    :return: adds an entry to each spectra that is a function of 2 others
    '''
    for spec in spectra:
        x = spec[key1]
        y = spec[key2]
        spec[entry_name] = function(x,y)
    return spectra

def spline_WS2_analysis_carbon(fn,gen_figures=False):
    '''
    :param fn: name of file containing map
    :return:  a spectra that has a full analysis, saving the file as a .p format in the same location
    '''
    spectra = import_raman(fn)
    print('imported')
    if 'fitted_spectrum' not in spectra[0]:
        spectra = get_WS2_fit_spline(spectra, 'data')
        print('peaks fitted')
    spectra = create_entry(spectra, '2D_G_ratio', '2D_height', 'G_height', lambda x, y: x / y)
    save_data(spectra,fn)
    print('data saved')

    #print('generating figures...')
    #generate_figures(spectra,fn)

    return  spectra