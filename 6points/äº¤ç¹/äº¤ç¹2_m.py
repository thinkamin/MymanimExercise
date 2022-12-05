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

        '''
        cir1 = Arc(start_angle=0,angle= 2*PI,radius=2,arc_center=ORIGIN)
        cir2 = Arc(start_angle=0,angle= 2*PI,radius=2,arc_center=UR)
        self.add(cir1,cir2)

        dot_r1 = SmallDot(cir1.arc_center).set_fill(color=BLUE)
        dot_r2 = SmallDot(cir2.arc_center).set_fill(color=BLUE)
        t1 = Text('A').next_to(dot_r1,UP)
        t2 = Text('B').next_to(dot_r2,UP)
        self.add(dot_r1,dot_r2,t1,t2)

        l_r = Line(cir1.arc_center,cir2.arc_center)
        self.add(l_r)
        '''

        #两个圆心不能为0或90度
        '''
        point1,point2 = get_intersect_cc(cir1,cir2)
        dotc =Dot(point1)
        dotd = Dot(point2)
        t3 = Text('C').next_to(dotc,UP)
        t4 = Text('D').next_to(dotd,UP)
        self.add(dotc,dotd,t3,t4)

        l_ac = Line(point1,cir1.arc_center)
        l_bc = Line(point1,cir2.arc_center)
        l_ad = Line(point2,cir1.arc_center)
        l_bd = Line(point2,cir2.arc_center)
        self.add(l_ac,l_bc,l_ad,l_bd)
        '''
        #两个圆心 0度
        cir1 = Arc(start_angle=0,angle= 2*PI,radius=2,arc_center=ORIGIN)
        cir2 = Arc(start_angle=0,angle= 2*PI,radius=1,arc_center=2*UP)
        point1,point2 = get_intersect_cc(cir1,cir2)
        dotc =Dot(point1)
        dotd = Dot(point2)
        self.add(cir1,cir2,dotc,dotd)




if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
