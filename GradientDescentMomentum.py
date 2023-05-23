import os
import sys
sys.path.append(os.getcwd())  # running manimgl from command line breaks imports on Stanley's computer w/o this line

from example_graphs import *
from GradientDescentBase import GradientDescentBase


class GradientDescentMomentum(GradientDescentBase):
    def __init__(self, zeros: list[float] = RANDOM_GRAPH[0], coef: float = RANDOM_GRAPH[1], dx: float = 1e-6,
                 start_x: float = 1, steps: int = 20, momentum: float = 0.4, **kwargs):
        super().__init__(zeros, coef, dx, start_x, steps, noisy=True, **kwargs)
        self.momentum = momentum
        self.prev_dx = None

    def gradient_descent(self, x: float, step: int) -> tuple[float, float]:
        derivative = (self.function(x + self.dx) - self.function(x - self.dx)) / (2 * self.dx)

        dx = -derivative if not self.prev_dx else -derivative + (self.prev_dx * self.momentum)
        self.prev_dx = dx
        return derivative, dx


def main():
    GradientDescentMomentum(*RANDOM_GRAPH).run()


if __name__ == "__main__":
    main()
