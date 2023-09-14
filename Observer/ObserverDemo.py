from Observer.ConcreteListenerA import ConcreteListenerA
from Observer.ConcretePublisher import ConcretePublisher


class ConcreteListenerB:
    pass


if __name__ == "__main__":
    # The client code.

    subject = ConcretePublisher()

    observer_a = ConcreteListenerA()
    subject.attach(observer_a)

    observer_b = ConcreteListenerB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()