from manimlib import *
from os import system
import numpy as np
import itertools as it
#import matplotlib.pyplot as plt

"""
2022-03-13

"""

'''
obj.set_stroke(color=RED,#width=15,opacity=1)
obj.set_fill(color=RED,#opacity=1)
path = TracedPath(obj.get_center,stroke_color=RED,stroke_width=12)
最终结果相关用红色
'''
class Test(Scene):
    def construct(self):
        #english_font = 'Times New Roman'
        #chinese_font = 'Microsoft YaHei'
        #color_map = it.cycle(BLUE,TEAL,GREEN,YELLOW,GOLD,RED,MAROON,PURPLE)#next(color_map)
        def point2dot_tex(point,a,position=UP,color=WHITE):
            dot = Dot(point).set_fill(color)
            t = Tex(a).next_to(dot,position)
            self.play(ShowCreation(dot),Write(t))
        def draw_line(point1,point2):
            line = Line(point1,point2).set_fill(color=RED)
            self.play(ShowCreation(line))

        grid = NumberPlane()
        self.add(grid)





if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
