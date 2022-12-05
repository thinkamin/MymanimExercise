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
        #一加dt变成不停了
        def anim(obj,dt):
            obj.rotate(0.001,about_point=ORIGIN)
        s1.add_updater(anim)
        self.wait(3)#3不起作用，会一直转下去




if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
