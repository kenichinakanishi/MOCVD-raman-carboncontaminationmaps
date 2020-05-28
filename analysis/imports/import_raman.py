def import_raman(fn):
    import numpy as np
    # This imports the raman spectra into a list of dictionary entries for analysis, containing all information.
    with open(fn, 'r') as f:
        # Opening the file and extracting the data by splitting it up and placing it in a numpy array
        rawdata = f.read().splitlines()[1:]
        rawdata = [line.split('\t') for line in rawdata]
        rawdata = np.array(rawdata).astype(np.float)

    spectra = []
    spectrum_wi = rawdata.copy()
    # spectrum_wi[:, 1] = spectrum_wi[:, 1] - np.min(spectrum_wi[:, 1])
    # spectrum_wi[:, 1] = spectrum_wi[:, 1] / np.max(spectrum_wi[:, 1])

    infodict = {'title': fn, 'data': spectrum_wi, 'x': 0, 'y': 0, 'sum_intensity': np.sum(rawdata[:, 1]),
                'max_intensity': np.max(rawdata[:, 1])}

    spectra.append(infodict)

    return spectra
