from manimlib import *
from os import system
import numpy as np
#import matplotlib.pyplot as plt

"""
2022-03-06

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

        # grid = NumberPlane()
        # self.add(grid)
        sq = Square().rotate(PI/4).set_fill(color=RED,opacity=1).set_stroke(color=RED)
        cir = Circle().set_fill(color='#333333',opacity=1)
        vg = VGroup(sq,cir)

        #这个方法说白了就是交叉并补呗
        self.add(vg)






if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
