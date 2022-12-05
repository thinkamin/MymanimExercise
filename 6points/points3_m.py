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
        cir = Circle()
        cir.data['points'][1]=np.array([2,0,0])
        self.add(cir)



if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
