from example_graphs import *
from GradientDescentBase import GradientDescentBase


class GradientDescentDecreasingStepSize(GradientDescentBase):
    def gradient_descent(self, x: float, step: int) -> tuple[float, float]:
        derivative = (self.function(x + self.dx) - self.function(x - self.dx)) / (2 * self.dx)
        return derivative, -derivative * (self.steps - step) / self.steps


def main():
    GradientDescentDecreasingStepSize(*OSCILLATING_GRAPH).run()


if __name__ == "__main__":
    main()
