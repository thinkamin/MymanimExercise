from manimlib import *
from os import system
import numpy as np
#import matplotlib.pyplot as plt

"""
2022-01-30

"""

class Test(Scene):
    def construct(self):
        grid = NumberPlane()
        self.add(grid)
        t_range=[0,2*np.pi]
        #中文
        text = Text('我爱你',font='Mrciosoft YaHei').scale(3)
        self.play(Write(text))
        text.shift(UP)
        #英文
        text = Text('SYlong presents',font='Times New Roman').scale(3)
        self.play(Write(text),run_time=5)

if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
