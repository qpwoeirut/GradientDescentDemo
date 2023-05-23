import math
from abc import ABCMeta, abstractmethod
from random import Random

from manimlib import *


class GradientDescentBase(Scene, metaclass=ABCMeta):
    def __init__(self, zeros: list[float], coef: float, dx: float = 1e-6, start_x: float = 1, steps: int = 20,
                 noisy: bool = False, **kwargs):
        super().__init__(**kwargs)

        self.zeros = zeros
        self.coef = coef
        self.dx = dx
        self.start_x = start_x
        self.steps = steps
        self.noisy = noisy

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
            derivative, step_value = self.gradient_descent(cur_x, step)
            if abs(derivative) < 5e-3:  # movements are essentially invisible at this point
                break

            derivative = round(derivative, ndigits=5)
            step_value = round(step_value, ndigits=5)

            derivative_text = Text(f"Derivative = {derivative}\nStep = {step_value}", font_size=40, font="serif",
                                   color=GREEN)
            derivative_text.move_to(dot)
            derivative_text.shift(np.array([0, 1, 0]))
            self.play(Write(derivative_text, run_time=1))
            self.wait(0.5)

            cur_x += step_value
            self.play(x_tracker.animate.set_value(cur_x), run_time=0.8)
            self.play(FadeOut(derivative_text))
            self.wait()

        dot.set_color(GREEN)

    @abstractmethod
    def gradient_descent(self, x: float, step: int) -> tuple[float, float]:
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
        y = self.coef * math.prod([x - zero for zero in self.zeros])
        if self.noisy:
            # use x as seed for new Random instance to ensure same value is generated
            seed = round(x / 4, ndigits=1) * 4
            noise = Random(x=seed).randint(-2, 2) * (0.1 - abs(seed - x))  # maximum of abs(seed - x) is 0.1
            y += noise
        return y
