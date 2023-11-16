import functools
from typing import Tuple, Callable

import numpy as np

from . import BaseFigure
from ._common import utils
from ._functions import dtft, magnitude
from ._sample_signal import get_x_range, get_sample_signal


class SignalAndDtftFigure(BaseFigure):
    x: np.ndarray
    sample_signal: np.ndarray

    x_range: np.ndarray

    def __init__(self, H_of_omega: Callable) -> None:
        super().__init__(H_of_omega)
        self.x, self.sample_signal = get_sample_signal()
        self.x_range = get_x_range()

    def _label_upper(self) -> Tuple[str, str]:
        return (r'(a) Waveform of signal $\it{x[n]}$',
                '')

    def _plot_upper(self, x: np.ndarray) -> None:
        self.upper.set_xticks(self.x_range, self.x_range)
        self.upper.set_xlabel(r' Sample number $\it{(n)}$')
        utils.do_plot(self.upper, self.x, self.sample_signal, y_limit=(-1, 1))

    def _label_lower(self) -> Tuple[str, str]:
        return (r'(b) Magnitude of DTFT of $\it{x[n]}$',
                r'$\mathregular{|X(e^{j\omega})|}$')

    def _plot_lower(self, x: np.ndarray) -> None:
        def do_dtft(omega) -> None:
            return magnitude(dtft(self.sample_signal, omega))
        utils.do_plot(self.lower, x, np.apply_along_axis(do_dtft, 0, x), y_limit=(0, 20))
