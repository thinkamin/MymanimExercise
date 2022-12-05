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
        l1=Line().shift(LEFT)
        l2=Line().rotate(PI/2).shift(LEFT/2)
        self.add(l1,l2)
        g1 = VGroup(l1,l2)
        #还是6个点
        print(g1.get_all_points())
        



if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
