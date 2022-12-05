from manimlib import *
from os import system
import numpy as np
#import matplotlib.pyplot as plt

"""
2022-01-28

"""

class Test(Scene):
    def construct(self):

        grid = NumberPlane()
        self.add(grid)

        circle = Circle()
        line = Line(np.array([0,0,0]),np.array([0,1,0]),color=RED)
        G = VGroup(circle,line)
        self.add(G)
        always_rotate(G,rate=90*DEGREES)
        #run_time能控制么？ 这个是不能

if __name__=="__main__":
    system('manimgl {}'.format(__file__)) 
