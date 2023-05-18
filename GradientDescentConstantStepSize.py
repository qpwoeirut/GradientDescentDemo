from example_graphs import *
from GradientDescentBase import GradientDescentBase


class GradientDescentConstantStepSize(GradientDescentBase):
    def gradient_descent(self, x: float, step: int) -> float:
        derivative = (self.function(x + self.dx) - self.function(x - self.dx)) / (2 * self.dx)
        return -derivative


def main():
    GradientDescentConstantStepSize(*TWO_MINIMA_GRAPH).run()


if __name__ == "__main__":
    main()