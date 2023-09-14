from typing import List

from Strategy import Strategy


class ConcreteReversed(Strategy):
    def do_algorithm(self, data: List):
        return reversed(sorted(data))
