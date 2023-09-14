from abc import abstractmethod, ABC
from typing import List


class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, data: List):
        pass
