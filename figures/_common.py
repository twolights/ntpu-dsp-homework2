import sys
from typing import Tuple, Callable

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from matplotlib.figure import Figure

sys.path.append(".")

import utils


class BaseFigure:
    figure: Figure
    upper: Axes
    lower: Axes
    H_of_omega: Callable

    def __init__(self, H_of_omega: Callable) -> None:
        self.figure, (self.upper, self.lower) = utils.create_standard_figure()
        self.H_of_omega = H_of_omega

    def _figure_title(self) -> str:
        raise NotImplementedError()

    def _label_upper(self) -> Tuple[str, str]:
        raise NotImplementedError()

    def _plot_upper(self, x: np.ndarray) -> None:
        raise NotImplementedError()

    def _label_lower(self) -> Tuple[str, str]:
        raise NotImplementedError()

    def _plot_lower(self, x: np.ndarray) -> None:
        raise NotImplementedError()

    def _plot(self) -> None:
        self.figure.suptitle(self._figure_title())

        x = utils.create_standard_x()
        upper_title, upper_y_label = self._label_upper()
        utils.label_plots(self.upper, title=upper_title, y_label=upper_y_label)
        self._plot_upper(x)

        lower_title, lower_y_label = self._label_lower()
        utils.label_plots(self.lower, title=lower_title, y_label=lower_y_label)
        self._plot_lower(x)

    def save(self, filename: str) -> None:
        self._plot()
        plt.savefig(filename)
        plt.close(self.figure)

    def show(self) -> None:
        self._plot()
        plt.show()
        plt.close(self.figure)
