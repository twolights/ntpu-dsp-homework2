from typing import Tuple

import numpy as np

from . import BaseFigure
from ._common import utils
from ._functions import hanning_window, dtft, magnitude

SIGNAL_STEP = 50
SIGNAL_TIME_START = 0
SIGNAL_TIME_STOP = 300
SIGNAL_TOTAL_POINTS = 301

SIGNAL_SIZE = 50

OMEGAS = [0.8 * np.pi, 0.2 * np.pi, 0.4 * np.pi]


class SignalAndDtftFigure(BaseFigure):
    y: np.ndarray

    @staticmethod
    def _find_index_for(x: np.ndarray, value: float):
        for i, v in enumerate(x):
            if v < value:
                continue
            return i
        return x.shape[0]

    @staticmethod
    def _create_sub_signal(M: int, omega: float) -> np.ndarray:
        y = np.ndarray(shape=(M, ))
        for i in range(0, M):
            y[i] = np.cos(omega * i)
        return hanning_window(M) * y

    def _label_upper(self) -> Tuple[str, str]:
        return (r'(a) Waveform of signal $\it{x[n]}$',
                '')

    def _setup_upper(self) -> None:
        x_range = np.arange(SIGNAL_TIME_START, SIGNAL_TIME_STOP + 1, step=SIGNAL_STEP)
        self.upper.set_xticks(x_range, x_range)

    def _plot_upper(self, x: np.ndarray) -> None:
        x = np.linspace(SIGNAL_TIME_START, SIGNAL_TIME_STOP, SIGNAL_TOTAL_POINTS)
        y = np.zeros_like(x)
        M = self._find_index_for(x, SIGNAL_SIZE)
        sub_signals = np.concatenate([self._create_sub_signal(M, omega) for omega in OMEGAS])
        length = sub_signals.shape[0]
        y[:length] = sub_signals
        self.upper.set_xlabel(r' Sample number $\it{(n)}$')
        self._setup_upper()
        utils.do_plot(self.upper, x, y, y_limit=(-1, 1))
        self.y = y

    def _label_lower(self) -> Tuple[str, str]:
        return (r'(b) Magnitude of DTFT of $\it{x[n]}$',
                r'$\mathregular{|X(e^{j\omega})|}$')

    def _plot_lower(self, x: np.ndarray) -> None:
        def do_dtft(omega):
            return magnitude(dtft(self.y, omega))
        utils.do_plot(self.lower, x, np.apply_along_axis(do_dtft, 0, x), y_limit=(0, 20))
