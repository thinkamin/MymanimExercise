from manimlib import *
from os import system
import numpy as np
#import matplotlib.pyplot as plt

"""
2022-03-03

"""

class Test(Scene):
    def construct(self):

        grid = NumberPlane()
        self.add(grid)

        s1 = Square().shift(LEFT)
        self.add(s1)
        # s1.add_updater(lambda a,dt:a.rotate(-3*dt,about_point=ORIGIN))
        s1.add_updater(lambda a,dt:a.shift(3*UP*dt))
        self.wait()



if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
