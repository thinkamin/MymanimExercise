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
        t = ValueTracker(0)
        def anim(obj):
            obj.become(Arc(start_angle=0,angle=t.get_value()%TAU))
        arc = Arc(angle=0).add_updater(anim)
        self.add(arc)
        self.play(t.set_value,2*TAU,run_time=8)



if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
