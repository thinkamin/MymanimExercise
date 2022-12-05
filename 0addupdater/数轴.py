from manimlib import *
from os import system
import numpy as np
import itertools as it
#import matplotlib.pyplot as plt

"""
2022-03-13

"""

'''
obj.set_stroke(color=RED,#width=15,opacity=1)
obj.set_fill(color=RED,#opacity=1)
path = TracedPath(obj.get_center,stroke_color=RED,stroke_width=12)
最终结果相关用红色
'''
class Test(Scene):
    def construct(self):
        t = ValueTracker(-2)

        numline = NumberLine()
        self.add(numline)
        triangle = Triangle().scale(0.1).move_to(np.array([-2,0.5,0]))
        dec = DecimalNumber(0)

        triangle.add_updater(lambda a:a.move_to(np.array([t.get_value(),0.5,0])))
        dec.add_updater(lambda a:a.set_value(t.get_value()))
        self.add(triangle,dec)
        self.play(t.animate.set_value(2),rate_function=linear,run_time=4)





if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
