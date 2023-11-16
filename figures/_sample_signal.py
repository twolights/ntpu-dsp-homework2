from typing import Tuple

import numpy as np

from ._functions import hanning_window

SIGNAL_STEP = 50
SIGNAL_TIME_START = 0
SIGNAL_TIME_STOP = 300
SIGNAL_TOTAL_POINTS = 301

SIGNAL_SIZE = 50

OMEGAS = [0.8 * np.pi, 0.2 * np.pi, 0.4 * np.pi]


def _find_index_for(x: np.ndarray, value: float) -> int:
    for i, v in enumerate(x):
        if v < value:
            continue
        return i
    return x.shape[0]


def _create_sub_signal(M: int, omega: float) -> np.ndarray:
    y = np.ndarray(shape=(M, ))
    for i in range(0, M):
        y[i] = np.cos(omega * i)
    return hanning_window(M) * y


def get_sample_signal() -> Tuple[np.ndarray, np.ndarray]:
    x = np.linspace(SIGNAL_TIME_START, SIGNAL_TIME_STOP, SIGNAL_TOTAL_POINTS)
    y = np.zeros_like(x)
    M = _find_index_for(x, SIGNAL_SIZE)
    sub_signals = np.concatenate([_create_sub_signal(M, omega) for omega in OMEGAS])
    length = sub_signals.shape[0]
    y[:length] = sub_signals
    return x, y


def get_x_range() -> np.ndarray:
    return np.arange(SIGNAL_TIME_START, SIGNAL_TIME_STOP + 1, step=SIGNAL_STEP)
