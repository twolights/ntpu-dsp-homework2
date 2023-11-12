from typing import Tuple, Optional

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from matplotlib.figure import Figure

DENSITY_OF_X = 1000

FIGURE_PADDING = 2.0
FIGURE_WIDTH = 8
FIGURE_HEIGHT = 6

DEFAULT_X_LABEL = r'$\mathregular{\omega}$'
DEFAULT_PI_INTERVAL = 0.2
PI_LITERAL = 'π'

TITLE_FONT_SIZE = 10
TITLE_Y = 0
TITLE_Y_PADDING = -35

LINE_WIDTH = 1.5
LINE_COLOR = 'darkslateblue'


def _init_plot_xticks(plot: Axes, pi_interval: float) -> None:
    def _populate_label(multiplier):
        if multiplier == 0:
            return '0'
        elif multiplier == -1:
            return '-' + PI_LITERAL
        elif multiplier == 1:
            return PI_LITERAL
        return f'{multiplier:.1f}' + PI_LITERAL

    x_range = np.arange(-np.pi, np.pi + np.pi * pi_interval, step=(np.pi * pi_interval))
    x_label_multipliers = np.arange(-1.0, 1.0 + pi_interval, step=pi_interval)
    x_labels = [_populate_label(i) for i in x_label_multipliers]
    plot.set_xticks(x_range, x_labels)


def _init_plot(plot: Axes) -> None:
    plot.grid(ls='--')
    _init_plot_xticks(plot, DEFAULT_PI_INTERVAL)


def create_standard_figure() -> Tuple[Figure, Tuple[Axes, Axes]]:
    figure, (upper, lower) = plt.subplots(2)
    figure.tight_layout(pad=FIGURE_PADDING)
    figure.set_figwidth(FIGURE_WIDTH)
    figure.set_figheight(FIGURE_HEIGHT)
    _init_plot(upper)
    _init_plot(lower)
    return figure, (upper, lower)


def label_plots(plot: Axes, title: str, y_label: str, x_label: Optional[str] = None) -> None:
    title_dict = {'fontsize': TITLE_FONT_SIZE}
    if x_label is None:
        x_label = DEFAULT_X_LABEL
    plot.set_title(title, y=TITLE_Y, pad=TITLE_Y_PADDING, verticalalignment="top", fontdict=title_dict)
    plot.set_ylabel(y_label)
    plot.set_xlabel(x_label)


def do_plot(plot: Axes, x: np.ndarray, y: np.ndarray,
            y_limit: Optional[Tuple[float, float]] = None) -> None:
    if y_limit is not None:
        bottom, top = y_limit
        plot.set_ylim(bottom=bottom, top=top)
    plot.plot(x, y, linewidth=LINE_WIDTH, c=LINE_COLOR)


def create_standard_x() -> np.ndarray:
    return np.linspace(-1 * np.pi, np.pi, num=int(2 * np.pi * DENSITY_OF_X))
