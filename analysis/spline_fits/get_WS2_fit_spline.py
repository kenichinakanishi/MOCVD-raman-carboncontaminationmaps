from .distribution_generators import *
def get_WS2_fit_spline(spectra, key):
    import numpy as np
    from scipy import interpolate
    import scipy.optimize as so
    guess = [340, 10, 1100, 0,  # first peak WS2 peak pos,width,height,offset
             420, 10, 1100, 0,  # second peak WS2
             1355, 100, 100, 0,  # D
             1585, 100, 100, 0,  # G
             2650, 1, 0.00001, 0]  # 2D

    bounds = ([328, 5, 5, 0,  # first peak WS2
               410, 5, 5, 0,  # second peak WS2
               1310, 50, 0.1, 0,
               1520, 50, 0.1, 0,
               2600, 0, 0, 0],

              [353, 33, 6000, 0.0001,  # first peak WS2
               430, 33, 6000, 0.0001,  # second peak WS2
               1400, 300, 400, 0.0001,  # D
               1640, 300, 400, 0.0001,  # G
               2700, 100, 0.0001, 0.0001])  # 2D

    print('Fitting spline version')

    for spec in spectra:
        w_i = spec[key].copy()
        spec['fitted_spectrum'] = w_i.copy()
        k = w_i[:, 0]
        amp = w_i[:, 1]
        anchor_points = [190, 258, 382, 500, 630, 760, 990, 1120, 1800, 1850];
        w = 3;
        anchor_x = []
        anchor_y = []

        for j in anchor_points:
            num = -1
            count = np.zeros(2000)
            average_amp = np.zeros(2000)
            average_pos = np.zeros(2000)
            for i in k:
                num = num + 1
                if j - w <= i <= j + w:
                    count[j] = count[j] + 1
                    average_amp[j] = average_amp[j] + amp[num]
                    average_pos[j] = average_pos[j] + i
            avg_amp = average_amp[j] / count[j]
            avg_pos = average_pos[j] / count[j]
            anchor_x.append(avg_pos)
            anchor_y.append(avg_amp)
        # print(spec['x'], spec['y'])

        tck = interpolate.splrep(anchor_x, anchor_y, s=0)
        interpolate_spline = interpolate.splev(k, tck)
        y_data = amp - interpolate_spline

        popt, pcov = so.curve_fit(lorentz, w_i[:, 0], y_data, p0=guess, bounds=bounds,
                                  maxfev=1000000000)
        perr = np.sqrt(np.diag(np.abs(pcov)))

        spec['WS1_pos'] = popt[0]
        spec['WS1_width'] = popt[1]
        spec['WS1_height'] = popt[2]
        spec['WS1_offset'] = popt[3]
        spec['WS1_pos_err'] = perr[0]
        spec['WS1_width_err'] = perr[1]
        spec['WS1_height_err'] = perr[2]

        spec['WS2_pos'] = popt[4]
        spec['WS2_width'] = popt[5]
        spec['WS2_height'] = popt[6]
        spec['WS2_offset'] = popt[7]
        spec['WS2_pos_err'] = perr[4]
        spec['WS2_width_err'] = perr[5]
        spec['WS2_height_err'] = perr[6]

        spec['D_pos'] = popt[8]
        spec['D_width'] = popt[9]
        spec['D_height'] = popt[10]
        spec['D_offset'] = popt[11]
        spec['D_pos_err'] = perr[8]
        spec['D_width_err'] = perr[9]
        spec['D_height_err'] = perr[10]

        spec['G_pos'] = popt[12]
        spec['G_width'] = popt[13]
        spec['G_height'] = popt[14]
        spec['G_offset'] = popt[15]
        spec['G_pos_err'] = perr[12]
        spec['G_width_err'] = perr[13]
        spec['G_height_err'] = perr[14]

        spec['2D_pos'] = popt[16]
        spec['2D_width'] = popt[17]
        spec['2D_height'] = popt[18]
        spec['2D_offset'] = popt[19]
        spec['2D_pos_err'] = perr[16]
        spec['2D_width_err'] = perr[17]
        spec['2D_height_err'] = perr[18]

        spec['fit_params'] = popt
        spec['fit_params_err'] = pcov
        spec['fitted_spectrum'][:, 1] = lorentz(w_i[:, 0], *popt) + interpolate_spline
        spec['background_spline'] = interpolate_spline
        spec['background_x'] = k

        lor_x = np.linspace(0, 1899, 1900)
        lor_W1 = np.linspace(0, 1899, 1900)
        lor_W2 = np.linspace(0, 1899, 1900)
        lor_D = np.linspace(0, 1899, 1900)
        lor_G = np.linspace(0, 1899, 1900)
        lor_D2 = np.linspace(0, 1899, 1900)

        WS1_pos = (spec['WS1_pos'])
        WS1_width = (spec['WS1_width'])
        WS1_height = (spec['WS1_height'])
        WS1_offset = (spec['WS1_offset'])
        WS2_pos = (spec['WS2_pos'])
        WS2_width = (spec['WS2_width'])
        WS2_height = (spec['WS2_height'])
        WS2_offset = (spec['WS2_offset'])
        D_pos = (spec['D_pos'])
        D_width = (spec['D_width'])
        D_height = (spec['D_height'])
        D_offset = (spec['D_offset'])
        G_pos = (spec['G_pos'])
        G_width = (spec['G_width'])
        G_height = (spec['G_height'])
        G_offset = (spec['G_offset'])
        D2_pos = (spec['2D_pos'])
        D2_width = (spec['2D_width'])
        D2_height = (spec['2D_height'])
        D2_offset = (spec['2D_offset'])

        for k in range(0, 1900):
            lor_W1[k] = lorentz(k, WS1_pos, WS1_width, WS1_height, WS1_offset)
            lor_W2[k] = lorentz(k, WS2_pos, WS2_width, WS2_height, WS2_offset)
            lor_D[k] = lorentz(k, D_pos, D_width, D_height, D_offset)
            lor_G[k] = lorentz(k, G_pos, G_width, G_height, G_offset)
            lor_D2[k] = lorentz(k, D2_pos, D2_width, D2_height, D2_offset)

        spec['WS1_area'] = np.trapz(lor_W1, lor_x)
        spec['WS2_area'] = np.trapz(lor_W2, lor_x)
        spec['D_area'] = np.trapz(lor_D, lor_x)
        spec['G_area'] = np.trapz(lor_G, lor_x)
        spec['2D_area'] = np.trapz(lor_D2, lor_x)

    return spectra
