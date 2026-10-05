par = {"a1": 2 / 3, "a2": 1, "b2": 2 / 3}


def lotka(t, vars, par):
    """
    Create the model equations using Scipy for integration (solve_ivp)

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
    X, Y = vars
    """
    Declare parameters
    """
    # Volume
    a1 = par.get("a1")
    a2 = par.get("a2")
    b2 = par.get("b2")
    """ 
    Declare fluxes
    """
    """
    Declare field
    """
    dX = a1 * X - a2 * X * Y
    dY = a2 * X * Y - b2 * Y
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
    return [x, x**0 * par["a1"] / par["a2"]]


def N_y(x, y, par) -> list:
    """
    y nullcline

    :param x: list
    :param y: list
    :param par: parameter set
    """
    return [par["b2"] / par["a2"] * x**0, y]


def eq(par) -> list:
    """
    Coordinates for the equilibrium point

    :param par: parameter set
    :return: Description
    :rtype: list
    """
    a1 = par["a1"]
    a2 = par["a2"]
    b1 = par["b1"]
    return [b1 / a2, a1 / a2]
