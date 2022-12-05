from manimlib import *
from os import system
import numpy as np
#import matplotlib.pyplot as plt

"""
2022-03-03
两个园那个
"""

class Test(Scene):
    def construct(self):

        grid = NumberPlane()
        self.add(grid)

        axe = Axes()
        vec1 = Vector(RIGHT,color=YELLOW)
        cir1 = Circle(radius=1,color=BLUE)
        g1 = VGroup(vec1,cir1)

        vec2 = Vector(RIGHT,color=YELLOW)
        cir2 = Circle(radius=1,color=BLUE)
        g2 = VGroup(vec2,cir2)

        g2.save_state()
        def anim1(obj,dt):
            obj.rotate(dt,about_point=ORIGIN)

        def anim2(obj):
            obj.restore()
            obj.rotate(-vec1.get_angle())
            obj.shift(vec1.get_vector())
        g1.add_updater(anim1)
        g2.add_updater(anim2)
        self.add(g1,g2)
        self.wait()




if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
