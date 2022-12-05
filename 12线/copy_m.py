from manimlib import *
from os import system
import numpy as np
#import matplotlib.pyplot as plt

"""
2022-03-05

"""

class Test(Scene):
    def construct(self):

        grid = NumberPlane()
        self.add(grid)

        line = Line(LEFT*1,UR*1)
        self.add(line)
        self.add(line.copy().rotate(PI/2).set_color(GREEN))



if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
