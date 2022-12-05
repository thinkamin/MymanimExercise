from manimlib import *
import numpy as np
class GraphExample(Scene):
    def construct(self):
        axes = Axes((-3, 10), (-1, 8))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        # input_to_graph_point == i2gp
        #你可以用i2gp来找到一个特定的点在图像上
        parabola = axes.get_graph(lambda x: 0.25 * x**2)
        parabola.set_stroke(BLUE)
        self.play(
            ShowCreation(parabola)
        )
        self.wait()

        dot = Dot(color=RED)
        dot.move_to(axes.i2gp(2, parabola))
        self.play(FadeIn(dot, scale=0.5))

        #value tracker 让我们动态一个参数，通常有mobject update 基于这个参数
        x_tracker = ValueTracker(2)
        # x_tracker = ValueTracker(3)
        f_always(
            dot.move_to,
            lambda: axes.i2gp(x_tracker.get_value(), parabola)
        )

        tan_line = always_redraw(lambda:axes.get_tangent_line(x_tracker.get_value(),parabola).scale(10))
        self.add(tan_line)

        self.play(x_tracker.animate.set_value(4), run_time=3)
        self.play(x_tracker.animate.set_value(-2), run_time=3)
        self.wait()


