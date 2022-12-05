from manimlib import *
from os import system
import numpy as np
import itertools as it
#import matplotlib.pyplot as plt

"""
2022-03-14

"""

'''
obj.set_stroke(color=RED,#width=15,opacity=1)
obj.set_fill(color=RED,#opacity=1)
path = TracedPath(obj.get_center,stroke_color=RED,stroke_width=12)
最终结果相关用红色
'''
class Test(Scene):
    def construct(self):

        grid = NumberPlane()

        cirb = Circle(radius=2.5)
        cirp = Circle(radius=3.5)
        cirt = Circle(radius=4.5)
        self.add(cirb,cirp,cirt)
        line_h = Line(2.5*RIGHT,4.5*RIGHT,color=BLUE)
        b_h = Brace(line_h,DOWN)
        self.add(line_h,b_h)
        r_h = Tex('h').next_to(b_h,DOWN)
        self.add(r_h)
        line_p = Line(ORIGIN,-3.5*RIGHT,color=YELLOW)
        b_p = Brace(line_p,DOWN)
        self.add(line_p,b_p)
        r_p = Tex('r_p').next_to(b_p,DOWN)
        self.add(r_p)





if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
