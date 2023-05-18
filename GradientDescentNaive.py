from example_graphs import *
from GradientDescentBase import GradientDescentBase


class GradientDescentNaive(GradientDescentBase):
    def gradient_descent(self, x: float) -> float:
        derivative = (self.function(x + self.dx) - self.function(x - self.dx)) / (2 * self.dx)
        return -derivative


def main():
    GradientDescentNaive(*TWO_MINIMA_GRAPH).run()


if __name__ == "__main__":
    main()
