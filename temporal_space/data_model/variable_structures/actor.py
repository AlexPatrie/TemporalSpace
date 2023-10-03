"""Object for holding Actor (variable) information"""


from abc import ABC, abstractmethod


class Actor(ABC):
    def __init__(self, name):
        super().__init__()
        self.name = name

    @abstractmethod
    def value(self):
        pass

