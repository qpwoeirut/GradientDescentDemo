from manimlib import *
from typing import Callable
import random


class GradientDescent(Scene):
    def construct(self) -> None:
        axes = Axes((-3, 10), (-1, 8))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))
        
        parabola = axes.get_graph(lambda x: 0.25 * x**2)
        parabola.set_stroke(BLUE)
        self.play(
            ShowCreation(parabola)
        )
        self.wait()

        current_x = 2

        # dot that follows graph
        dot = Dot(color=RED)
        dot.move_to(axes.i2gp(current_x, parabola))
        self.play(FadeIn(dot, scale=0.5))

        x_tracker = ValueTracker(current_x)
        f_always(
            dot.move_to,
            lambda: axes.i2gp(x_tracker.get_value(), parabola)
        )

        for _ in range(10):
            current_x += self.gradient_descent(parabola, current_x)
            self.play(x_tracker.animate.set_value(current_x), run_time=0.5)

        self.wait()

    # takes a function and the current point, returns how much to step in a direction
    # TODO: right now it just steps towards x=5
    @staticmethod
    def gradient_descent(f: Callable[[int], int], x: int) -> int:
        return (5 - x) / 3

