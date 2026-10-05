from numpy import sqrt

# field_forsterling parameters
kR2 = 3e6
kR3 = 2
kR4 = 3e3
kR5 = 42

# law of mass action conversion
H = 0.8
k1 = kR3 * H**2
k2 = kR2 * H
k3 = kR5 * H
k4 = kR4
k5 = 0.3
A = 0.06
B = 0.03

# Parameter formulas
alpha = (2 * k4) / (k3 * A)
beta = k2 / (k3 * A)
gamma = (k4 * k5 * B) / (k3 * A) ** 2
delta = k5 * B
f = 1
mu = 0.02
scale_u = k3 * A
scale_v = (k2 * k3 * A) / (2 * k4)
scale_w = k5 * B
eps = scale_w / scale_u

par = {
    "k1": k1,
    "k2": k2,
    "k3": k3,
    "k4": k4,
    "k5": k5,
    "A": A,
    "B": B,
    "mu": mu,
    "f": 1,
    "alpha": alpha,
    "beta": beta,
    "gamma": gamma,
    "delta": delta,
    "epsilon": eps,
}


def oregonator(t, vars, par):
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
    u, w = vars
    """
    Declare parameters
    """
    # Volume
    f = par.get("f")
    eps = par.get("epsilon")
    mu = par.get("mu")
    """
    Declare fluxes
    """
    """
    Declare field
    """
    du = (1 / eps) * (u - u**2 - f * w * ((u - mu) / (u + mu)))
    dw = u - w
    field = [du, dw]
    """
    Return
    """
    return field


def N_u(u, w, par) -> list:
    """
    x nullcline

    :param x: list
    :param y: list
    :param par: parameter set
    """
    f = par.get("f")
    mu = par.get("mu")
    return [u, (u / f) * ((u + mu - u**2 - u * mu) / (u - mu))]


def N_w(u, w, par) -> list:
    """
    y nullcline

    :param x: list
    :param y: list
    :param par: parameter set
    """
    return [u, u]


def eq(par) -> list:
    """
    Coordinates for the equilibrium point

    :param par: parameter set
    :return: Description
    :rtype: list
    """
    f = par.get("f")
    mu = par.get("mu")
    eq = 1 / 2 * (1 - mu - f + sqrt((mu + f - 1) ** 2 + 4 * mu * (f + 1)))
    return [eq, eq]
