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
            y[i + 1:] -= np.sign(diff) * 2 * np.pi  # TODO a bit brute-forced, see if can be improved
    if normalize:
        y -= y[middle_index]  # normalize to value at 0
    return y


def magnitude(x: complex):
    return np.sqrt(x.real ** 2 + x.imag ** 2)


def group_delay(phase_H: np.ndarray, d_omega: float):
    y = np.zeros_like(phase_H)
    length = y.shape[0] - 1
    for i, v in enumerate(phase_H):
        if i == length:
            break
        # grp[H(e^jw)] = -d(angle H(e^jw))/d_omega
        y[i] = -1 * (phase_H[i + 1] - v) / d_omega
    return y


def hanning_window(M: int):
    result = np.ndarray(shape=(M, ))
    for n in range(0, M):
        result[n] = 0.5 - 0.5 * np.cos(2 * np.pi * n / (M - 1))
    return result


def dtft(y: np.ndarray, omega: float):
    result = 0 + 0j
    for n, v in enumerate(y):
        result += v * np.exp(-1j * omega * n)
    return result
