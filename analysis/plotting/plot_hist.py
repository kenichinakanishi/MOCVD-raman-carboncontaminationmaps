def plot_hist(spectra, key, statistics=False, show=True):
    import numpy as np
    import matplotlib.pyplot as plt
    x = np.zeros(len(spectra))
    for i in range(len(spectra)):
        spec = spectra[i]
        x[i] = spec[key]
    bins = int(len(spectra) / 10)
    mu = x.mean()
    median = np.median(x)
    sigma = x.std()
    x[np.abs(x) > 30 * np.abs(median)] = median
    mu = x.mean()
    median = np.median(x)
    sigma = x.std()
    v_max = mu + 3 * sigma
    v_min = mu - 3 * sigma

    if key == 'D_height':
        v_max = 300
        v_min = 0
    elif key == 'WS1_height':
        v_max = 3000
        v_min = 0
    elif key == 'WS2_height':
        v_max = 1500
        v_min = 0
    elif key == 'G_height':
        v_max = 150
        v_min = 0
    elif key == 'D_area':
        v_min = 0
    elif key == 'G_area':
        v_min = 0
    elif key == 'WS1_area':
        v_min = 0
    elif key == 'WS2_area':
        v_min = 0
    else:
        v_max = mu + 3 * sigma
        v_min = mu - 3 * sigma

    textstr = '$\mu=%.2f$\n$\mathrm{median}=%.2f$\n$\sigma=%.2f$' % (mu, median, sigma)
    fig, ax = plt.subplots(figsize=(10, 4));
    ax.hist(x, bins, range=(v_min, v_max));
    plt.title('Histogram of %s' % key);
    plt.xlabel(key);
    plt.ylabel('Frequency');
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax.text(0.75, 0.95, textstr, transform=ax.transAxes, fontsize=14,
            verticalalignment='top', bbox=props)
    if show:
        plt.show();
    else:
        return plt.gcf();
