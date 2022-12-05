from manimlib import *
from os import system
import numpy as np
#import matplotlib.pyplot as plt

"""
2022-03-05

"""

class Test(Scene):
    def construct(self):
        line = Line(LEFT*3,UR*3)
        self.add(line)
        dot = Dot(line.point_from_proportion(0.5)).set_color(color=RED)
        self.add(dot)
        #三等分点同理 alpha换成0.33




if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
