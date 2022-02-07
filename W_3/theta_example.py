import numpy as np


def l2_norm(x):
    x_norm = x * x
    x_norm = np.sum(x_norm)
    x_norm = np.sqrt(x_norm)
    return x_norm


def angle(x, y):
    v = np.inner(x, y) / (l2_norm(x) * l2_norm(y))
    theta = np.arccos(v)
    return theta


x = np.array([1, -1, 1, -1], int)
y = np.array([4, -4, 4, -4], int)

print(np.inner(x, y))

