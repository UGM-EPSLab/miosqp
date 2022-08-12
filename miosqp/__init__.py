from .constants import *  # noqa: F401
from .data import add_bounds  # noqa: F401
from .default_settings import MIOSQP_SETTINGS, OSQP_SETTINGS  # noqa: F401
from .solver import MIOSQP  # noqa: F401

__MIOSQP_VERSION__ = '0.0.1'
__EPSLAB_FORK_VERSION__ = '0.0.1'

__version__ = f"{__MIOSQP_VERSION__}.{__EPSLAB_FORK_VERSION__}"

# This (EPSLab/epslab/utils/miosqp) is based on
# https://github.com/osqp/miosqp/tree/master/miosqp
