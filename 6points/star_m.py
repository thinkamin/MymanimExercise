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
        star = RegularPolygon(4)
        ratio = 0.9
        star.data['points'][1::3]-=star.data['points'][1::3]*ratio
        self.add(star)



if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
