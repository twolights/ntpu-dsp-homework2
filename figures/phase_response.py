from typing import Tuple

import numpy as np

from . import BaseFigure
from ._common import utils

UNWRAP_RADIAN_THRESHOLD = 5


class PhaseResponseFigure(BaseFigure):
    @staticmethod
    def ARG(x: complex):
        return np.arctan2(x.imag, x.real)

    @staticmethod
    def unwrap_ARG(y: np.ndarray):
        y = np.array(y, copy=True)
        length = y.shape[0] - 1
        middle_index = int(length / 2)
        for i, v in enumerate(y):
            if i == 0 or i == length:
                continue
            diff = (y[i + 1] - v)
            if np.abs(diff) > UNWRAP_RADIAN_THRESHOLD:
                y[i + 1:] -= np.sign(diff) * 2 * np.pi
        y -= y[middle_index]  # normalize to value at 0
        return y

    def _label_upper(self) -> Tuple[str, str]:
        return ('(a) Principal Value of Phase Response',
                r'$\mathregular{ARG[H(e^{j\omega})]}$')

    def _plot_upper(self, x: np.ndarray):
        def principal_phase_of_H(omega: float):
            return self.ARG(self.H_of_omega(omega))

        utils.do_plot(self.upper,
                      x, np.apply_along_axis(principal_phase_of_H, 0, x),
                      y_limit=(-4, 4))

    def _label_lower(self) -> Tuple[str, str]:
        return ('(b) Unwrapped Phase Response',
                r'$\mathregular{arg[H(e^{j\omega})]}$')

    def _plot_lower(self, x: np.ndarray):
        def principal_phase_of_H(omega: float):
            return self.ARG(self.H_of_omega(omega))

        y = self.unwrap_ARG(np.apply_along_axis(principal_phase_of_H, 0, x))

        utils.do_plot(self.lower, x, y)
