from abc import ABC, abstractmethod
from Observer.Publisher import Publisher


class Listener(ABC):
    @abstractmethod
    def update(self, publisher: Publisher) -> None:
        pass
