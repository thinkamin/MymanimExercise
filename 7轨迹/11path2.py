from manimlib import *
from os import system
import numpy as np

"""
2021-12-13

"""

class Test(Scene):
    def construct(self):
        '''
        轨迹 需要：
        1 起点 终点
        2 中间点
        3ValueTracker （0-1）
        '''
        grid = NumberPlane()
        self.add(grid)
        start = Dot(color=RED)
        end = Dot(color=BLUE).shift(RIGHT*2)
        self.add(start,end)
        t = ValueTracker(0)
        b= Dot().add_updater(lambda m:m.move_to((end.get_center()-start.get_center())*t.get_value()))

        path = TracedPath(b.get_center,stroke_width=5,stroke_color=RED)
        self.add(path,b)
        # self.add(b)
        self.play(end.animate.shift(UP*2),t.increment_value,1,run_time=7,rate_func=linear)

if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
