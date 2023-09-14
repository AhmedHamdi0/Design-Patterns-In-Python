from abc import ABC, abstractmethod
from Observer.Listener import Listener


class Publisher(ABC):
    @abstractmethod
    def attach(self, listener: Listener) -> None:
        pass

    @abstractmethod
    def detach(self, listener: Listener) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass
