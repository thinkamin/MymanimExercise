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

        points = [
                np.array([1,0,0]),
                np.array([2,1,0]),
                np.array([0,-1,0])
                ]

        print(bezier(points))



if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
