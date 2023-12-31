from typing import Tuple

import numpy as np
from . import BaseFigure
from ._common import utils
from ._functions import ARG, unwrap_ARG, magnitude, group_delay


class GroupDelayFigure(BaseFigure):
    def _figure_title(self) -> str:
        return 'Figure B - Group Delay and Magnitude'

    def _label_upper(self) -> Tuple[str, str]:
        return (r'(a) Group delay of $\it{H(z)}$',
                r'$\mathregular{grd[H(e^{j\omega})]}$')

    def _plot_upper(self, x: np.ndarray) -> None:
        def principal_phase_of_H(omega: float):
            return ARG(self.H_of_omega(omega))

        phase_H = unwrap_ARG(np.apply_along_axis(principal_phase_of_H, 0, x))
        d_omega = x[1] - x[0]
        utils.do_plot(self.upper, x, group_delay(phase_H, d_omega))

    def _label_lower(self) -> Tuple[str, str]:
        return ('(b) Magnitude of Frequency Response',
                r'$\mathregular{\left|H(e^{j\omega})\right|}$')

    def _plot_lower(self, x: np.ndarray) -> None:
        def magnitude_of_H(omega: float):
            return magnitude(self.H_of_omega(omega))

        utils.do_plot(self.lower, x, np.apply_along_axis(magnitude_of_H, 0, x))
