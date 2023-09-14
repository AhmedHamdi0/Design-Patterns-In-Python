from typing import List

from Strategy import Strategy


class ConcreteSorted(Strategy):
    def do_algorithm(self, data: List):
        return sorted(data)
