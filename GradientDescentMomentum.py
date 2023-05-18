from example_graphs import *
from GradientDescentBase import GradientDescentBase


class GradientDescentMomentum(GradientDescentBase):
    def __init__(self, zeros: list[float], coef: float, dx: float = 1e-6, start_x: float = 1, steps: int = 20, momentum: float = 0.4, **kwargs):
        super().__init__(zeros, coef, dx, start_x, steps, **kwargs)
        self.momentum = momentum
        self.prev_dx = None

    def gradient_descent(self, x: float, step: int) -> float:
        derivative = (self.function(x + self.dx) - self.function(x - self.dx)) / (2 * self.dx)

        dx = -derivative if not self.prev_dx else -derivative + (self.prev_dx * self.momentum)
        self.prev_dx = dx
        return dx


def main():
    GradientDescentMomentum(*TWO_MINIMA_GRAPH, start_x=3, momentum=0.7).run()


if __name__ == "__main__":
    main()
