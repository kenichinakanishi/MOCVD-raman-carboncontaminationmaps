def plot_map(spectra, key, show=False):
    import numpy as np
    import matplotlib.pyplot as plt
    x = []
    y = []
    z = []
    for spec in spectra:
        x.append(spec['x'])
        y.append(spec['y'])
        z.append(spec[key])
    x = np.array(x)
    y = np.array(y)
    z = np.array(z)
    min_x = min(x)
    min_y = min(y)
    x = x - min_x
    y = y - min_y
    std = np.std(z)
    med = np.median(z)
    mean = np.mean(z)
    # z[np.abs(z) > 30*np.abs(med)] = med
    mean = z.mean()
    med = np.median(z)
    std = z.std()
    x = np.unique(x)
    y = np.unique(y)
    X, Y = np.meshgrid(x, y)
    Z = z.reshape(len(y), len(x))
    v_max = mean + 3 * std
    v_min = mean - 3 * std

    plt.clf();

    if key == 'D_height':
        v_max = 300
        v_min = 0
    elif key == 'WS1_height':
        v_max = 3000
        v_min = 0
    elif key == 'WS2_height':
        v_max = 2000
        v_min = 0
    elif key == 'G_height':
        v_max = 300
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
        v_max = mean + 3 * std
        v_min = mean - 3 * std

    plt.pcolormesh(X, Y, Z, cmap='inferno', vmin=v_min, vmax=v_max, shading='flat');

    cbar = plt.colorbar();
    cbar.set_label(key);
    fig = plt.gcf();
    fig.set_size_inches(10, 8);
    plt.rcParams.update({'font.weight': 'medium'})
    plt.rcParams.update({'xtick.labelsize': 16})
    plt.rcParams.update({'ytick.labelsize': 16})
    plt.rcParams.update({'axes.labelsize': 18})
    plt.rcParams.update({'axes.linewidth': 1.5})
    plt.rcParams.update({'xtick.major.pad': 10})
    plt.rcParams.update({'ytick.major.pad': 10})
    plt.rcParams.update({'xtick.major.size': 6})
    plt.rcParams.update({'ytick.major.size': 6})
    plt.rcParams.update({'xtick.major.width': 1.5})
    plt.rcParams.update({'ytick.major.width': 1.5})
    plt.rcParams.update({'lines.linewidth': 2})
    if show:
        plt.show();
    else:
        return plt.gcf();
