from typing import Tuple

import numpy as np

from . import BaseFigure
from ._common import utils
from ._functions import hanning_window, dtft, magnitude
from ._sample_signal import get_x_range, get_sample_signal


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
        x_range = get_x_range()
        self.upper.set_xticks(x_range, x_range)

    def _plot_upper(self, x: np.ndarray) -> None:
        x, y = get_sample_signal()
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
