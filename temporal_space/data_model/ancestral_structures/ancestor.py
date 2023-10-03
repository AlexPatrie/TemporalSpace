"""Ancestral class which exists at the 0th index of the overall data structure.


Expected to be in the schema of:

D = {
  tPrimeN: {
    tStepN: [
      XtStepN,
      YtStepN,
      ZtStepN,
    ],
  },
}

...where tPrimeN is the index position of the outer global timestep, and X, Y, Z are cartesian
coordinates at the given monotonically decreasing id of `tStepN`.


"""

from abc import ABC, abstractmethod
from typing import *
from temporal_space.data_model.time_structures.tstep import Tstep
from temporal_space.data_model.index_structures.tstep_index import TstepIndex


class TemporalAncestor(ABC):
    t_primes: List[Dict[TstepIndex, Tstep]]

    def __init__(self, n_tprime: int):
        self.n_tprime = n_tprime
        self.t_primes = self._generate_primes()

    @abstractmethod
    def _generate_primes(self):
        pass
