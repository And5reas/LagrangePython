import numpy as np


def calc(x: tuple, y: tuple, projetar):
    k = 0
    s = 0
    if len(x) != len(y):
        raise Exception("Sorry the tuples must be ordered pair (Must have the same amount of values in the tuples)")
    for i in x:
        v = 1
        for j in x:
            if i != j:
                # Doing L math '-'
                # Ex. | L = (X - X2) * (X - X3) |
                #     |     (X - X2) * (X - X3) |
                v = np.polymul(v, np.poly1d([1, -j])) / (i-j)
        # Sum f(X1) * L1 + f(X2) * L2 + ... + f(Xn) * Ln:
        s = np.polyadd(s, np.polymul(y[k], v))
        k += 1
    # project a point
    return np.polyval(s, projetar)


print(calc((-1, 0, 1, 2), (2, 0, 1, 4), 6))
