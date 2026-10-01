par = {
    'alpha': 1, 
    'beta': 2.5, 
    'k': 1
}

def brusselator(t, vars, par):
    """
    Create the model equations using Scipy for integration (solve_ivp)
    Model without CDI
    
    Parameters
    ----------
    t: double
            time 
    y: vector 
            state variables
    par: dict 
            dictionary with parameters

    Returns 
    ----------
    field: vector 
            field equations
    """

    """
    Declare variables
    """
    x, y = vars
    """
    Declare parameters 
    """
    #Volume
    alpha = par.get('alpha')
    beta = par.get('beta')
    k = par.get('k')
    """ 
    Declare fluxes 
    """
    """
    Declare field 
    """
    dX= alpha - beta*x + x**2*y - k*x
    dY= beta*x - x**2*y
    field = [dX, dY]
    """
    Return
    """
    return field 

def N_x(x, y, par) -> list: 
    """
    x nullcline 
    
    :param x: list
    :param y: list
    :param par: parameter set
    """ 
    alpha = par.get('alpha')
    beta = par.get('beta')
    k = par.get('k')
    return [x, ((beta + k)*x - alpha)/(x**2)]

def N_y(x, y, par) -> list: 
    """
    y nullcline 
    
    :param x: list
    :param y: list
    :param par: parameter set
    """
    alpha = par.get('alpha')
    beta = par.get('beta')
    k = par.get('k')
    return [x, beta/x]

def eq(par) -> list:
    """
    Coordinates for the equilibrium point
    
    :param par: parameter set
    :return: Description
    :rtype: list
    """
    alpha = par.get('alpha')
    beta = par.get('beta')
    k = par.get('k')
    return [alpha/k, k*beta/alpha]

def trapping_lines(x, y):
    l1 = [[0, 5], [0.05,0.05]]
    l2 = [[0.05,0.05], [0,5]]
    l3 = [x, 6 - x]
    l4 = [x, 3.5 + x]
    return [l1, l2, l3, l4]

def trapping_lines_markers():
    epsx = 0.2
    epsy = 0.2
    l1 = [epsx, 2]
    l2 = [2, epsy]
    l3 = [4 - 2*epsx, 2]
    l4 = [0.8, 3.5 + 0.8 - epsy]
    return [l1, l2, l3, l4]

def trapping_lines_ics():
    l1 = [0, 2]
    l2 = [2, 0]
    l3 = [3, 3]
    l4 = [0.8, 3.5 + 0.8]
    return [l1, l2, l3, l4]