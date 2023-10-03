from abc import ABC, abstractmethod


class Index(ABC):
    value: object

    def __init__(self):
        super().__init__()
        self.value = self._set_value()

    @abstractmethod
    def _set_value(self, val=None):
        pass

