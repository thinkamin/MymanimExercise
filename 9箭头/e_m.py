from manimlib import *
from os import system
import numpy as np
import itertools as it
#import matplotlib.pyplot as plt

"""
2022-03-19

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
        self.add(grid)

        t1 = Tex('\\lim_{n \\to \\infty}(1+\\frac{1}{n})^n=e=2.718281828\\dots')
        t2 = Tex('e=\\sum_{n=0}^{\\infty}(\\frac{1}{n!})')
        t3 = Tex('=\\frac 1 {0!} +\\frac 1 {1!} +\\frac 1 {2!}+\\frac 1 {3!}+\\dots')
        t4 = Tex('=1+1+\\frac 1 2 +\\frac 1 6 +\\dots')
        vg = VGroup()
        vg.add(t1,t2,t3,t4).arrange(DOWN)
        self.add(vg)






if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
