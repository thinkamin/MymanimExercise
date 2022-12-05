from manimlib import *
from os import system
import numpy as np

"""
2021-12-13

"""

class Test(Scene):
    def construct(self):
        grid = NumberPlane()
        self.add(grid)

        dot = Dot()
        self.play(dot.shift,RIGHT*3,
                rate_func=smooth,run_time=10)

        dot.shift(-3*RIGHT)
        self.play(dot.shift,RIGHT*3,
                rate_func=linear,run_time=10)
        dot.shift(-3*RIGHT)
        self.play(dot.shift,RIGHT*3,
                rate_func=rush_into,run_time=10)
        dot.shift(-3*RIGHT)
        self.play(dot.shift,RIGHT*3,
                rate_func=there_and_back,run_time=10)
        dot.shift(-3*RIGHT)
        self.play(dot.shift,RIGHT*3,
                rate_func=there_and_back_with_pause,run_time=10)


if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
