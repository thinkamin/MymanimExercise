from manimlib import *
from os import system
import numpy as np
import itertools as it
#import matplotlib.pyplot as plt

"""
2022-03-11

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
        t1 = Text("简化的思想:整体换元法，倒数换元法")
        t2 = Text("转化的思想:根号变平方,分式变整式")
        t3 = Text("分析的思想:分类")




if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
