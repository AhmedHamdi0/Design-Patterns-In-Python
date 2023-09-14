from Observer.Listener import Listener
from Observer.Publisher import Publisher


class ConcreteListenerA(Listener):
    def update(self, publisher: Publisher) -> None:
        if publisher._state == 0 or publisher._state >= 2:
            print("ConcreteListenerB: Reacted to the event")
