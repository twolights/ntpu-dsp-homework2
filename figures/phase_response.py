import functools
from typing import Tuple, Callable

import numpy as np

from . import BaseFigure
from ._common import utils
from ._functions import ARG, unwrap_ARG


class PhaseResponseFigure(BaseFigure):
    principal_phase_of_H: Callable

    def __init__(self, H_of_omega: Callable) -> None:
        def principal_phase_of_H(H: Callable, omega: float):
            return ARG(H(omega))

        super().__init__(H_of_omega)
        self.principal_phase_of_H = functools.partial(principal_phase_of_H, H_of_omega)

    def _label_upper(self) -> Tuple[str, str]:
        return ('(a) Principal Value of Phase Response',
                r'$\mathregular{ARG[H(e^{j\omega})]}$')

    def _plot_upper(self, x: np.ndarray) -> None:
        utils.do_plot(self.upper,
                      x, np.apply_along_axis(self.principal_phase_of_H, 0, x),
                      y_limit=(-4, 4))

    def _label_lower(self) -> Tuple[str, str]:
        return ('(b) Unwrapped Phase Response',
                r'$\mathregular{arg[H(e^{j\omega})]}$')

    def _plot_lower(self, x: np.ndarray) -> None:
        y = unwrap_ARG(np.apply_along_axis(self.principal_phase_of_H, 0, x))
        utils.do_plot(self.lower, x, y)
