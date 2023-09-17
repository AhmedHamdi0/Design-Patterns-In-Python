from Facade.Facade import Facade
from Facade.Subsystem1 import Subsystem1
from Facade.Subsystem2 import Subsystem2
from Facade.client_code import client_code

if __name__ == "__main__":
    # The client code may have some of the subsystem's objects already created.
    # In this case, it might be worthwhile to initialize the Facade with these
    # objects instead of letting the Facade create new instances.
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)
