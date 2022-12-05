from manimlib import *
from os import system
import numpy as np
#import matplotlib.pyplot as plt

"""
2022-01-30

"""

class Test(Scene):
    def construct(self):
        grid = NumberPlane()
        self.add(grid)
        #1 点
        d = Dot(color=RED) 
        self.add(d)
        #2 轨迹
        path = TracedPath(d.get_center,stroke_color=RED)
        self.add(path)
        #path之后才能加点的运用,顺序是重点
        #其实path与valuetracker结合是很好的
        #3play
        self.play(d.animate.move_to(np.array([1,1,0])))

if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
