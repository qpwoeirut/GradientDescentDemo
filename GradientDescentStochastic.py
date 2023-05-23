import os
import sys

sys.path.append(os.getcwd())  # running manimgl from command line breaks imports on Stanley's computer w/o this line

from example_graphs import *
from GradientDescentBase import GradientDescentBase
from manimlib import *


class GradientDescentStochastic(GradientDescentBase):
    def __init__(self, **kwargs):
        super().__init__(*RANDOM_GRAPH, steps=20, **kwargs)
        self.graph = None
        self.to_fade = []

    def construct(self) -> None:
        self.graph = self.setup_scene()

        cur_x = self.start_x[0]

        # dot that follows graph
        dot = Dot(color=RED)
        dot.move_to(self.axes.i2gp(cur_x, self.graph))
        self.play(FadeIn(dot, scale=0.5))

        x_tracker = ValueTracker(cur_x)
        f_always(dot.move_to, lambda: self.axes.i2gp(x_tracker.get_value(), self.graph))

        fails_in_a_row = 0
        fails_text = Text("Fails: 0")
        fails_text.to_corner(TOP + RIGHT)
        self.add(fails_text)
        for step in range(self.steps):
            derivative, step_value = self.gradient_descent(cur_x, step)
            if step_value == 0:  # movements are essentially invisible at this point
                fails_in_a_row += 1
                if fails_in_a_row == 5:
                    self.play(*map(FadeOut, self.to_fade), run_time=0.6)
                    self.to_fade.clear()
                    self.wait()

                    dot.set_color(GREEN)
                    self.wait(3)  # give a bit of extra buffer time
                    break
            else:
                fails_in_a_row = 0
            fails_text.become(Text(f"Fails: {fails_in_a_row}"))
            fails_text.to_corner(TOP + RIGHT)
            self.add(fails_text)

            step_value = round(step_value, ndigits=5)

            cur_x += step_value
            self.play(x_tracker.animate.set_value(cur_x), *map(FadeOut, self.to_fade), run_time=0.6)
            self.to_fade.clear()
            self.wait()

    def gradient_descent(self, x: float, step: int) -> tuple[float, float]:
        x_l = x + (random.randint(-10, -1) / 10) * (self.steps - step) / self.steps
        self.show_guess(x_l, ORANGE, RIGHT)

        x_r = x + (random.randint(1, 10) / 10) * (self.steps - step) / self.steps
        self.show_guess(x_r, PURPLE, LEFT)

        if min(self.function(x_l), self.function(x), self.function(x_r)) == self.function(x):
            return self.derivative(x), 0
        elif self.function(x_l) <= self.function(x_r):
            return self.derivative(x), x_l - x
        else:
            return self.derivative(x), x_r - x

    def show_guess(self, x, color, edge):
        dot = Dot(color=color)
        dot.move_to(self.axes.i2gp(x, self.graph))
        self.play(FadeIn(dot, scale=0.5), run_time=0.1)

        text = Text(f"x = {round(x, ndigits=4)}\ny = {round(self.function(x), ndigits=4)}", color=color, font_size=30)
        text.move_to(dot, aligned_edge=edge)
        text.shift(np.array([0, 1, 0]))
        self.play(Write(text, run_time=0.5))

        self.to_fade.append(dot)
        self.to_fade.append(text)


def main():
    GradientDescentStochastic().run()


if __name__ == "__main__":
    main()
