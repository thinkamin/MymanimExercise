from manimlib import *
from os import system
import numpy as np
import itertools as it
#import matplotlib.pyplot as plt

"""
2022-03-14

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

        grid = NumberPlane()
        self.add(grid)

        a = np.linspace(0,1,5)#[0,1,n] n等分
        line = Line(LEFT*2,RIGHT*2)
        for i in a:
            print(i)
            dot = Dot(line.point_from_proportion(i))
            self.add(dot)
        self.add(line)
        





if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
