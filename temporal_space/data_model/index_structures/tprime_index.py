from abc import abstractmethod
from typing import Tuple
from temporal_space.data_model.index_structures._index import Index


class TprimeIndex(Index):
    def __init__(self, prefix: int, suffix: int):
        """I.E: `0 0` or `4 3` so: `outer inner`"""
        super().__init__()
        self.prefix = prefix
        self.suffix = suffix

    def _set_value(self, val=None) -> Tuple:
        pass
