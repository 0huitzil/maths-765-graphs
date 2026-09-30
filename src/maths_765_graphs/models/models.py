import numpy as np
from scipy.integrate import solve_ivp

def getIVP(model, par, ics, tini=0, tf=100): 
    """
    Simple integration using the solve_ivp routine from Scipy 

    Parameters
    ----------
    model: func
            model to integrate
    par: dict 
            set of named parameters 
    ics: dict
            set of named initial conditions
    tini: double
            start of integration time
    tf: double
            end of integration time 

    Returns 
    ----------
    data: array, first entry is t value, rest of values are the model variables
    """
    data = solve_ivp(model, [tini, tini+tf],list(ics.values()), method = 'Radau', max_step = 500, rtol = 1e-7, atol = 1e-9, args = (par,))
    data = np.vstack((data.t, data.y))
    return data