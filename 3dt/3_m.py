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

        s1 =Square()
        self.add(s1)
        s1.add_updater(lambda a,dt:a.rotate(TAU*0.08*dt))
        self.wait(5)
        s1.clear_updaters()



if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
