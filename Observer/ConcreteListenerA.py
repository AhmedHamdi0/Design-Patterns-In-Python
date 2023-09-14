from Observer.Listener import Listener
from Observer.Publisher import Publisher


class ConcreteListenerA(Listener):
    def update(self, publisher: Publisher) -> None:
        if publisher._state < 3:
            print("ConcreteListenerA: Reacted to the event")
