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


        s1 = Circle().set_fill(color=YELLOW,opacity=0.4).to_corner(UL)
        self.add(s1)
        s4 = RegularPolygon(4)
        s5 = RegularPolygon(5).scale(2)
        #这个也是存在问题
        s4.reverse_points()
        vg = VGroup(s4,s5).set_fill(color=YELLOW,opacity=0.4)
        #不明白为什么s4更深一些
        self.add(vg)




if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
