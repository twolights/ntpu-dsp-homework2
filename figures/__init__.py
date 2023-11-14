from typing import Callable

from ._common import BaseFigure

from .phase_response import PhaseResponseFigure
from .group_delay import GroupDelayFigure
from .signal_and_dtft import SignalAndDtftFigure

ALL = 'all'
FIGURE_CLASS_MAPPING = {
    'a': PhaseResponseFigure,
    'b': GroupDelayFigure,
    'c': SignalAndDtftFigure,
}
AVAILABLE_FIGURES = FIGURE_CLASS_MAPPING.keys()


def get_figure(identifier: str, H_of_omega: Callable) -> BaseFigure:
    if identifier not in FIGURE_CLASS_MAPPING:
        raise RuntimeError(f'Cannot find figure ({identifier})')
    klass = FIGURE_CLASS_MAPPING[identifier]
    return klass(H_of_omega)
