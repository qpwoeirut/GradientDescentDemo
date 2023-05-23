import os
import sys
sys.path.append(os.getcwd())  # running manimgl from command line breaks imports on Stanley's computer w/o this line

from example_graphs import *
from GradientDescentBase import GradientDescentBase


class GradientDescentRestarts(GradientDescentBase):
    def __init__(self, **kwargs):
        super().__init__(*RANDOM_GRAPH, start_x=[3, 1, 6], show_derivative=False, **kwargs)

    def gradient_descent(self, x: float, step: int) -> tuple[float, float]:
        derivative = (self.function(x + self.dx) - self.function(x - self.dx)) / (2 * self.dx)
        return derivative, -derivative * (self.steps - step) / self.steps


def main():
    GradientDescentRestarts().run()


if __name__ == "__main__":
    main()
