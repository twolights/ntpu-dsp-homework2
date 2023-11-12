from typing import Tuple

import numpy as np

from . import BaseFigure
from ._common import utils


class PhaseResponseFigure(BaseFigure):
    @staticmethod
    def ARG(x: complex):
        return np.arctan2(x.imag, x.real)

    @staticmethod
    def unwrap_ARG(y: np.ndarray):
        # TODO unwrap here
        y = np.array(y, copy=True)
        return y

    # TODO remove this one
    @staticmethod
    def arg(x: complex):
        return np.arctan(x.imag / x.real)

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
        def continue_phase_of_H(omega: float):
            # TODO return self.unwrap_ARG(self.ARG(self.H_of_omega(omega)))
            return self.arg(self.H_of_omega(omega))

        utils.do_plot(self.lower, x, np.apply_along_axis(continue_phase_of_H, 0, x))
