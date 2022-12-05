from manimlib import *
from os import system
import numpy as np
#import matplotlib.pyplot as plt

"""
2022-03-10

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
        #color_map = (BLUE,TEAL,GREEN,YELLOW,GOLD,RED,MAROON,PURPLE)

        grid = NumberPlane()
        self.add(grid)
        line = Line(LEFT*2,RIGHT*2)
        self.add(line)
        p1,p2=line.get_start_and_end()
        length=get_norm(p1-p2)
        print(length)




if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
