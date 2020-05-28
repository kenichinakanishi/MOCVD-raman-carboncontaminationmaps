def get_average_spec(spectra):
    key = 'data'
    average = np.zeros_like(spectra[0][key][:,0])
    for spec in spectra:
        average += spec[key][:,1]*spec['max_intensity']

    average = average/len(spectra)
    avgdata = spectra[0][key].copy()
    avgdata[:,1] = average
    plt.plot(avgdata[:,0],avgdata[:,1])
    plt.show()
    return average
