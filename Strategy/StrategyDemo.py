from ConcreteReversed import ConcreteReversed
from ConcreteSorted import ConcreteSorted
from Context import Context

if __name__ == "__main__":
    context = Context(ConcreteSorted())
    print("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic()

    print()
    print("Client: Strategy is set to reverse sorting.")
    context.strategy = ConcreteReversed()
    context.do_some_business_logic()
