from manimlib import *
from os import system
import numpy as np

"""
2022-03-05

"""

class Test(Scene):
    def construct(self):

        grid = NumberPlane()
        self.add(grid)

        cir =Circle()
        a = PointIndex(cir)
        self.add(a)
        



if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
