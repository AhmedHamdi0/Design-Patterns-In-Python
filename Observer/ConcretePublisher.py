from random import randrange
from typing import List
from poetry.publishing import Publisher
from Observer.Listener import Listener


class ConcretePublisher(Publisher):
    _state: int = None
    _listeners: List[Listener] = []

    def attach(self, listener: Listener) -> None:
        print("Publisher: Attached an listener.")
        self._listeners.append(listener)

    def detach(self, listener: Listener) -> None:
        print("Publisher: Detached an listener.")
        self._listeners.remove(listener)

    def notify(self) -> None:
        print("Publisher: Notifying listeners...")
        for listener in self._listeners:
            listener.update(self)

    def some_business_logic(self) -> None:
        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()
