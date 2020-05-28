def import_raman_map2(fn):
    import os
    import numpy as np
    if os.path.isfile(fn[:-4] + '.p'):
        print('data loaded from pickle')
        return load_data(fn)
    else:
        # This imports the raman spectra into a list of dictionary entries for analysis, containing all information.
        with open(fn, 'r') as f:
            # Opening the file and extracting the data by splitting it up and placining it in a numpy array
            rawdata = f.read().splitlines()[1:]
            rawdata = [line.split('\t') for line in rawdata]
            rawdata = np.array(rawdata).astype(np.float)

        spectra_length = int(len([row for row in rawdata if row[0] == rawdata[0, 0] and row[1] == rawdata[0, 1]]))
        total_pixels = int(rawdata.shape[0] / spectra_length)
        x_pixels = int(len([row for row in rawdata if row[1] == rawdata[0, 1]]) / spectra_length)
        y_pixels = int(len([row for row in rawdata if row[0] == rawdata[0, 0]]) / spectra_length)

        x_range = np.abs(rawdata[0, 0] - rawdata[-1, 0])
        y_range = np.abs(rawdata[0, 1] - rawdata[-1, 1])
        dx = x_range / (x_pixels - 1)
        dy = y_range / (y_pixels - 1)

        spectra = []
        for i in range(total_pixels):
            spectrum_wi = np.zeros([spectra_length, 2])
            rawchunk = rawdata[i * spectra_length:(i + 1) * spectra_length, :]
            spectrum_wi[:, 0] = rawchunk[:, 2]
            spectrum_wi[:, 1] = (rawchunk[:, 3]) - (np.min(rawchunk[:, 3]))
            spectrum_wi[:, 1] = spectrum_wi[:, 1] * 4
            infodict = {}
            infodict['title'] = fn
            infodict['data'] = spectrum_wi
            infodict['x'] = rawchunk[0, 0]
            infodict['y'] = rawchunk[0, 1]
            infodict['sum_intensity'] = np.sum(rawchunk[:, 3])
            infodict['max_intensity'] = np.max(rawchunk[:, 3])
            # spectrum_wi[:, 1] = spectrum_wi[:, 1] / np.max(spectrum_wi[:, 1])
            spectra.append(infodict)
        return spectra
