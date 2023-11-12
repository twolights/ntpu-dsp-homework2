import numpy as np

UNWRAP_RADIAN_THRESHOLD = 5


def ARG(x: complex):
    return np.arctan2(x.imag, x.real)


def unwrap_ARG(y: np.ndarray, normalize: bool = True):
    y = np.array(y, copy=True)
    length = y.shape[0] - 1
    middle_index = int(length / 2)
    for i, v in enumerate(y):
        if i == 0 or i == length:
            continue
        diff = (y[i + 1] - v)
        if np.abs(diff) > UNWRAP_RADIAN_THRESHOLD:
            y[i + 1:] -= np.sign(diff) * 2 * np.pi
    if normalize:
        y -= y[middle_index]  # normalize to value at 0
    return y


def magnitude(x: complex):
    return np.sqrt(x.real ** 2 + x.imag ** 2)
