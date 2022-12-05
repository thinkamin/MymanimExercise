from manimlib import *
from os import system
import numpy as np
#import matplotlib.pyplot as plt

"""
2022-01-31

"""

class Test(Scene):
    def construct(self):

        grid = NumberPlane()
        self.add(grid)

        t_range=(0,2*PI)
        func2 = ParametricCurve(
                lambda t:np.array([
                    t-np.sin(t),
                    1-np.cos(t),
                    0
                    ]),t_range
                )
        self.play(ShowCreation(func2))


if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
