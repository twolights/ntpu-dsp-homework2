from typing import Tuple

import numpy as np

from . import BaseFigure
from ._common import utils
from ._functions import ARG, unwrap_ARG


class PhaseResponseFigure(BaseFigure):
    def _label_upper(self) -> Tuple[str, str]:
        return ('(a) Principal Value of Phase Response',
                r'$\mathregular{ARG[H(e^{j\omega})]}$')

    def _plot_upper(self, x: np.ndarray):
        def principal_phase_of_H(omega: float):
            return ARG(self.H_of_omega(omega))

        utils.do_plot(self.upper,
                      x, np.apply_along_axis(principal_phase_of_H, 0, x),
                      y_limit=(-4, 4))

    def _label_lower(self) -> Tuple[str, str]:
        return ('(b) Unwrapped Phase Response',
                r'$\mathregular{arg[H(e^{j\omega})]}$')

    def _plot_lower(self, x: np.ndarray):
        def principal_phase_of_H(omega: float):
            return ARG(self.H_of_omega(omega))

        y = unwrap_ARG(np.apply_along_axis(principal_phase_of_H, 0, x))

        utils.do_plot(self.lower, x, y)
