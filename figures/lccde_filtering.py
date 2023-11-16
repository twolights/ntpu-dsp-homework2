import functools
from typing import Tuple, Callable, Union

import numpy as np

from . import BaseFigure
from ._common import utils
from ._sample_signal import get_x_range, get_sample_signal

SIGNAL_STEP = 50
SIGNAL_TIME_START = 0
SIGNAL_TIME_STOP = 300
SIGNAL_TOTAL_POINTS = 301

OMEGAS = [0.8 * np.pi, 0.2 * np.pi, 0.4 * np.pi]

SIGNAL_SIZE = 50


def _LCCDE_prototype(a: Union[list, np.ndarray],
                     b: Union[list, np.ndarray],
                     n: int,
                     x: np.ndarray, y: np.ndarray) -> complex:
    def _value_or_initial_rest(o: np.ndarray, index: int):
        if index < 0:
            return 0
        return o[index]

    return (b[0] / a[0]) * _value_or_initial_rest(x, n) \
        + (b[1] / a[0]) * _value_or_initial_rest(x, n - 1) \
        + (b[2] / a[0]) * _value_or_initial_rest(x, n - 2) \
        - (a[1] / a[0]) * _value_or_initial_rest(y, n - 1) \
        - (a[2] / a[0]) * _value_or_initial_rest(y, n - 2)


class LCCDEFilteringFigure(BaseFigure):
    x: np.ndarray
    sample_signal: np.ndarray

    x_range: np.ndarray

    @classmethod
    def _create_LCCDE(cls, a: Union[list, np.ndarray], b: Union[list, np.ndarray]) -> Callable:
        return functools.partial(_LCCDE_prototype, a, b)

    @classmethod
    def _c_of_k(cls, k: int):
        return 0.95 * np.exp(1j * (0.15 * np.pi + 0.02 * np.pi * k))

    @classmethod
    def _H2_c_of_k(cls, k: int):
        c_k = cls._c_of_k(k)
        c_k_star = np.conj(c_k)
        a = [1, -1 * (c_k + c_k_star), 0.95 ** 2]
        b = [0.95 ** 2, -1 * (c_k + c_k_star), 1]
        return cls._create_LCCDE(a, b)

    def __init__(self, H_of_omega: Callable) -> None:
        super().__init__(H_of_omega)
        self.x, self.sample_signal = get_sample_signal()
        self.x_range = get_x_range()

    def _label_upper(self) -> Tuple[str, str]:
        return (r'(a) Waveform of LCCDE processed signal $\it{y[n]}$',
                '')

    def _plot_upper(self, x: np.ndarray) -> None:
        H1 = self._create_LCCDE(
            [1, -0.8 * (np.exp(0.4 * np.pi * 1j) + np.exp(-0.4 * np.pi * 1j)), 0.8 ** 2],
            [1, -0.98 * (np.exp(0.8 * np.pi * 1j) + np.exp(-0.8 * np.pi * 1j)), 0.98 ** 2]
        )
        H2 = [self._H2_c_of_k(k + 1) for k in range(0, 4)]
        y = np.zeros_like(self.x)
        length = y.shape[0]
        for i in range(0, length):
            y[i] = H1(i, self.sample_signal, y)
        for H2_k in H2:
            for _ in range(0, 2):
                signal_after_H = y.copy()
                y = np.zeros_like(y)
                for i in range(0, length):
                    y[i] = H2_k(i, signal_after_H, y)
        self.upper.set_xlabel(r' Sample number $\it{(n)}$')
        self.upper.set_xticks(self.x_range, self.x_range)
        utils.do_plot(self.upper, self.x, y)

    def _label_lower(self) -> Tuple[str, str]:
        return (r'(b) Waveform of original signal $\it{x[n]}$',
                '')

    def _plot_lower(self, x: np.ndarray) -> None:
        self.lower.set_xticks(self.x_range, self.x_range)
        self.lower.set_xlabel(r' Sample number $\it{(n)}$')
        utils.do_plot(self.lower, self.x, self.sample_signal)
