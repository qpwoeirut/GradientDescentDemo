import math
from abc import ABCMeta, abstractmethod
from manimlib import *


class GradientDescentBase(Scene, metaclass=ABCMeta):
    def __init__(self, zeros: list[float], coef: float, dx: float = 1e-6, start_x: float = 1, steps: int = 20, **kwargs):
        super().__init__(**kwargs)

        self.zeros = zeros
        self.coef = coef
        self.dx = dx
        self.start_x = start_x
        self.steps = steps

        self.min_x = math.ceil(min(self.zeros + [-1]) - 2)
        self.max_x = math.ceil(max(self.zeros + [1]) + 2)
        self.max_y = math.ceil(max(self.function(self.min_x + 1), self.function(self.max_x - 1)))

    def construct(self) -> None:
        axes = Axes((self.min_x, self.max_x), (-self.max_y, self.max_y))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        graph = axes.get_graph(self.function)
        graph.set_stroke(BLUE)
        self.play(ShowCreation(graph))
        self.wait()

        cur_x = self.start_x

        # dot that follows graph
        dot = Dot(color=RED)
        dot.move_to(axes.i2gp(cur_x, graph))
        self.play(FadeIn(dot, scale=0.5))

        x_tracker = ValueTracker(cur_x)
        f_always(dot.move_to, lambda: axes.i2gp(x_tracker.get_value(), graph))

        for step in range(self.steps):
            cur_x += self.gradient_descent(cur_x, step)
            self.play(x_tracker.animate.set_value(cur_x), run_time=0.5)

        self.wait()

    @abstractmethod
    def gradient_descent(self, x: float, step: int) -> float:
        """
        Takes an x-value and returns how much to step in the x direction.
        Should implement a gradient descent method that works on self.function
        """
        raise NotImplementedError("this should be implemented in a subclass!")

    def function(self, x: float) -> float:
        """
        Defines the function to graph, which is also the function we'll run gradient descent on
        :param x: the x-value on the graph
        :return: the y-value (equivalent to f(x))
        """
        return self.coef * math.prod([x - zero for zero in self.zeros])
