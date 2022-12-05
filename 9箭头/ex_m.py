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
        # self.add(grid)
        t1 = Tex('e^{ix}=1+\\frac {ix}{1!}+\\frac {(ix)^2}{2!}+\\frac {(ix)^3}{3!}+\\frac {(ix)4}{4!}+\\dots+\\frac {(ix)^n}{n!}')
        t2 = Tex('e^{ix}=1-\\frac {x^2}{2!}+\\frac {x^4}{4!}-\\frac {x^6}{6!}\\dots+i(\\frac x {1!}-\\frac {x^3} {3!}+\\frac {x^5}{5!}\\dots)') 
        t3 = Tex('\\because cosx=1-\\frac{x^2}{2!}+\\frac{x^4}{4!}-\\frac{x^6}{6!}\\dots')
        t4 = Tex('\\because sinx=x-\\frac{x^3}{3!}+\\frac{x^5}{5!}-\\frac{x^7}{7!}\\dots')
        t5 = Tex('e^{ix}=cosx+isinx')
        vg = VGroup(t1,t2,t3,t4,t5).arrange(DOWN)
        self.add(vg)






if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
