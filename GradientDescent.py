from manimlib import *

RANDOM_GRAPH = ([-2, 1, 5, 5], 0.005)
OSCILLATING_GRAPH = ([0, 0], 1)
TWO_MINIMA_GRAPH = ([-4, 0, 2, 2], 0.05)


class GradientDescent(Scene):
    def __init__(self, zeros: list[float], coef: float, dx: float = 1e-6, **kwargs):
        super().__init__(**kwargs)

        self.zeros = zeros
        self.coef = coef
        self.dx = dx

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

        cur_x = 2

        # dot that follows graph
        dot = Dot(color=RED)
        dot.move_to(axes.i2gp(cur_x, graph))
        self.play(FadeIn(dot, scale=0.5))

        x_tracker = ValueTracker(cur_x)
        f_always(dot.move_to, lambda: axes.i2gp(x_tracker.get_value(), graph))

        for _ in range(25):
            cur_x += self.gradient_descent(cur_x)
            self.play(x_tracker.animate.set_value(cur_x), run_time=0.4)

        self.wait()

    # takes a function and the current point, returns how much to step in a direction
    def gradient_descent(self, x: int) -> float:
        derivative = (self.function(x + self.dx) - self.function(x - self.dx)) / (2 * self.dx)
        return -derivative

    def function(self, x: float) -> float:
        return self.coef * math.prod([x - zero for zero in self.zeros])


def main():
    GradientDescent(*TWO_MINIMA_GRAPH).run()


if __name__ == "__main__":
    main()
