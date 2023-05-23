import os
import sys
sys.path.append(os.getcwd())  # running manimgl from command line breaks imports on Stanley's computer w/o this line

from example_graphs import *
from GradientDescentBase import GradientDescentBase


class GradientDescentMomentum(GradientDescentBase):
    def __init__(self, momentum: float = 0.7, **kwargs):
        super().__init__(*TWO_MINIMA_GRAPH, start_x=3.5, **kwargs)
        self.momentum = momentum
        self.prev_dx = None

    def gradient_descent(self, x: float, step: int) -> tuple[float, float]:
        derivative = self.derivative(x)

        dx = -derivative if not self.prev_dx else -derivative + (self.prev_dx * self.momentum)
        self.prev_dx = dx
        return derivative, dx


def main():
    GradientDescentMomentum().run()


if __name__ == "__main__":
    main()
