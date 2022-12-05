from manimlib import *
from os import system
import numpy as np
#import matplotlib.pyplot as plt

"""
2022-03-04

"""

class Test(Scene):
    def construct(self):

        grid = NumberPlane()
        self.add(grid)

        line = Line(LEFT*4,RIGHT*4,color=BLUE).shift(UP*2.5)
        cir = Circle().shift(LEFT*3+DOWN).scale(2)
        sinfunc=ParametricCurve(
                lambda t:np.array([t,np.sin(t),0]),
                t_min=-PI/2,
                t_max=PI/2
                ).shift(RIGHT*2+DOWN).set_color(YELLOW)
        dot_o=Dot()
        dot_1=Dot()
        dot_2=Dot()
        def anim0(obj,alpha):
            obj.move_to(line.point_from_proportion(alpha))

        def anim1(obj,alpha):
            obj.move_to(cir.point_from_proportion(alpha))

        def anim2(obj,alpha):
            obj.move_to(sinfunc.point_from_proportion(alpha))
        self.add(line,cir,dot_o,dot_1,dot_2,sinfunc)
        self.play(UpdateFromAlphaFunc(dot_o,anim0),
                UpdateFromAlphaFunc(dot_1,anim1),
                UpdateFromAlphaFunc(dot_2,anim2),
                run_time=10)


if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
