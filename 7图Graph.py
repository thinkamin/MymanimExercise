from manimlib import *
import numpy as np

# To watch one of these scenes, run the following:
# manimgl example_scenes.py OpeningManimExample
# Use -s to skip to the end and just save the final frame
# Use -w to write the animation to a file
# Use -o to write it to a file and open it once done
# Use -n <number> to skip ahead to the n'th animation of a scene.


class GraphExample(Scene):
    def construct(self):
        axes = Axes((-3, 10), (-1, 8))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        #axes.get_graph 将会返回一个函数图像
        sin_graph = axes.get_graph(
            lambda x: 2 * math.sin(x),
            color=BLUE,
        )
        #默认地 它会在x，f(x)平滑的插值，如果图像有棱角，那么设置use_smoothing为False
        relu_graph = axes.get_graph(
            lambda x: max(x, 0),
            use_smoothing=False,#这一句是重点
            color=YELLOW,
        )
        #对于不连续的函数，你可以指定不连续的点，因此它不会试着将缝隙连起来
        step_graph = axes.get_graph(
            lambda x: 2.0 if x > 3 else 1.0,
            discontinuities=[3],#这一句是重点
            color=GREEN,
        )

        # Axes.get_graph_label 输入一个string或者mobject
        #图示如果是String 以latex对待 默认在右边一点 颜色与图像一致
        sin_label = axes.get_graph_label(sin_graph, "\\sin(x)")
        relu_label = axes.get_graph_label(relu_graph, Text("ReLU"))
        step_label = axes.get_graph_label(step_graph, Text("Step"), x=4)

        self.play(
            ShowCreation(sin_graph),
            FadeIn(sin_label, RIGHT),
        )
        self.wait(2)
        self.play(
            ReplacementTransform(sin_graph, relu_graph),
            FadeTransform(sin_label, relu_label),
        )
        self.wait()
        self.play(
            ReplacementTransform(relu_graph, step_graph),
            FadeTransform(relu_label, step_label),
        )
        self.wait()

        
