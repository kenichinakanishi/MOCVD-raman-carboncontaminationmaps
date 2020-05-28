def lorentz(x, *params):
    import numpy as np
    # This function is a simple lorentzian generator given the parameters in the form :
    # [center, FWHM (Gamma), amplitude, y-offset, center2, FWHM2,...]
    # for as many peaks as there are sets of 4 parameters. The x coordinates are that entered in the spectrum.
    y = np.zeros_like(x)
    for i in range(0, len(params), 4):
        ctr = params[i]
        gam = params[i + 1]
        amp = params[i + 2]
        con = params[i + 3]
        y = y + amp * (0.5 * gam) ** 2 / ((x - ctr) ** 2 + (gam * 0.5) ** 2) + con
    return y
