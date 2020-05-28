from analysis.spline_fits import *
def plot_samples_spline(spectra, key1, key2, no_samples=9):
    import numpy as np
    import matplotlib.pyplot as plt
    no_figures = int(np.ceil(np.sqrt(no_samples)))
    lor_x = np.linspace(0, 1899, 1900)
    lor_W1 = np.linspace(0, 1899, 1900)
    lor_W2 = np.linspace(0, 1899, 1900)
    lor_D = np.linspace(0, 1899, 1900)
    lor_G = np.linspace(0, 1899, 1900)
    lor_D2 = np.linspace(0, 1899, 1900)
    WS1_pos = (spectra[0]['WS1_pos'])
    WS1_width = (spectra[0]['WS1_width'])
    WS1_height = (spectra[0]['WS1_height'])
    WS1_offset = (spectra[0]['WS1_offset'])
    WS2_pos = (spectra[0]['WS2_pos'])
    WS2_width = (spectra[0]['WS2_width'])
    WS2_height = (spectra[0]['WS2_height'])
    WS2_offset = (spectra[0]['WS2_offset'])
    D_pos = (spectra[0]['D_pos'])
    D_width = (spectra[0]['D_width'])
    D_height = (spectra[0]['D_height'])
    D_offset = (spectra[0]['D_offset'])
    G_pos = (spectra[0]['G_pos'])
    G_width = (spectra[0]['G_width'])
    G_height = (spectra[0]['G_height'])
    G_offset = (spectra[0]['G_offset'])
    D2_pos = (spectra[0]['2D_pos'])
    D2_width = (spectra[0]['2D_width'])
    D2_height = (spectra[0]['2D_height'])
    D2_offset = (spectra[0]['2D_offset'])
    interpolate_spline = (spectra[0]['background_spline'])
    interpolate_x = (spectra[0]['background_x'])

    for k in range(0, 1900):
        lor_W1[k] = lorentz(k, WS1_pos, WS1_width, WS1_height, WS1_offset)
        lor_W2[k] = lorentz(k, WS2_pos, WS2_width, WS2_height, WS2_offset)
        lor_D[k] = lorentz(k, D_pos, D_width, D_height, D_offset)
        lor_G[k] = lorentz(k, G_pos, G_width, G_height, G_offset)
        lor_D2[k] = lorentz(k, D2_pos, D2_width, D2_height, D2_offset)
    plt.clf
    plt.subplots(no_figures, no_figures)
    for i in range(no_figures):
        for j in range(no_figures):
            spectrum = spectra[np.random.randint(0, len(spectra))]
            d1 = spectrum[key1]
            d2 = spectrum[key2]
            plt.subplot(no_figures, no_figures, i * no_figures + j + 1)
            plt.plot(d1[:, 0], d1[:, 1])
            plt.plot(d2[:, 0], d2[:, 1], alpha=0.5)
            plt.plot(lor_x, lor_W1)
            plt.plot(lor_x, lor_W2)
            plt.plot(lor_x, lor_D)
            plt.plot(lor_x, lor_G)
            plt.plot(lor_x, lor_D2)
            plt.plot(interpolate_x, interpolate_spline)
    plt.style.use('ggplot')
    fig = plt.gcf()
    plt.title(spectra[0]['title'][38:])
    fig.set_size_inches(10, 8)
    plt.show()
