import os
import sys
sys.path.append(os.getcwd())  # running manimgl from command line breaks imports on Stanley's computer w/o this line

from example_graphs import *
from GradientDescentBase import GradientDescentBase


class GradientDescentDecreasingStepSize(GradientDescentBase):
    def __init__(self, **kwargs):
        super().__init__(*OSCILLATING_GRAPH, **kwargs)

    def gradient_descent(self, x: float, step: int) -> tuple[float, float]:
        derivative = self.derivative(x)
        return derivative, -derivative * (self.steps - step) / self.steps


def main():
    GradientDescentDecreasingStepSize().run()


if __name__ == "__main__":
    main()
