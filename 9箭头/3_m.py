from manimlib import *
from os import system
import numpy as np
#import matplotlib.pyplot as plt

"""
2022-03-07

"""

'''
obj.set_stroke(color=RED,#width=15,opacity=1)
obj.set_fill(color=RED,#opacity=1)
path = TracedPath(obj.get_center,stroke_color=RED,stroke_width=12)
'''
class Test(Scene):
    def construct(self):
        #english_font = 'Times New Roman'
        #chinese_font = 'Microsoft YaHei'

        grid = NumberPlane()
        self.add(grid)
        tex1 = Tex('e^{i\\theta} = a+bi')
        self.add(tex1)



if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
