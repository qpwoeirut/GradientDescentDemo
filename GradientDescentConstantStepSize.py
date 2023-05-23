import sys, os
sys.path.append(os.getcwd())  # running manimgl from command line breaks imports on Stanley's computer w/o this line

from example_graphs import *
from GradientDescentBase import GradientDescentBase


class GradientDescentConstantStepSize(GradientDescentBase):
    def gradient_descent(self, x: float, step: int) -> tuple[float, float]:
        derivative = (self.function(x + self.dx) - self.function(x - self.dx)) / (2 * self.dx)
        return derivative, -derivative


def main():
    GradientDescentConstantStepSize(*TWO_MINIMA_GRAPH).run()


if __name__ == "__main__":
    main()
