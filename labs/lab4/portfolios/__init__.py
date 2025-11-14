from .portfolios import Portfolios
from .portfolios_load import portfolios_load
from .portfolios_save import portfolios_save

# Attach dynamic methods to the class
Portfolios.load = portfolios_load
Portfolios.save = portfolios_save

__all__ = ["Portfolios"]
