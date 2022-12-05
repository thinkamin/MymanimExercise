from manimlib import *
from os import system
import numpy as np
#import matplotlib.pyplot as plt

"""
2022-03-05

"""

class Test(Scene):
    def construct(self):

        s1 = Square(side_length=0.5).set_fill(color=RED,opacity=1).get_grid(3,3)
        # s1.set_color(BLUE)
        #从左上到右下梯度上色
        s1.set_color_by_gradient(GREEN,RED,BLUE)
        self.add(s1)
            



if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
