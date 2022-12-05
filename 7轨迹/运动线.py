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

        cir = Circle().shift(UP).set_stroke(color=YELLOW)
        dot = Dot()
        g1 = VGroup(cir,dot)
        g1.save_state()
        def anim(obj,alpha):
            obj.restore()
            obj.shift(6*RIGHT*alpha)
            obj.rotate(TAU*alpha,axis=IN)
        path = TracedPath(dot.get_center,stroke_color=RED,stroke_width=5)
        self.add(g1,path)
        # self.play()
        self.play(UpdateFromAlphaFunc(g1,anim),run_time=10)



if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
