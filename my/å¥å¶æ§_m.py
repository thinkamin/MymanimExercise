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
        problem=Text('已知f(x+1)是奇函数，f(x+2)是偶函数')
        t1 = Tex('f((x+1)+1)=-f(-(x+1)+1)')
        t2 = Tex('f(x+2)=-f(x)')
        t3 = Tex('f(x+4)=f(x+2+2)')
        t4 = Tex('f(x+2+2)=-f(x+2)')
        t5 = Tex('\\because f(x+2)=-f(x)')
        t11 = Tex('\\therefore f(x+4)=f(x)')
        t6 = Tex('\\because f(x+1)=-f(-x+1)')
        t7 = Tex('x+1=-x+1')
        t8 = Tex('x=0')
        t9 = Tex('f(1)=-f(1)')
        t10 = Tex('f(1)=0')
        vg =VGroup(problem,t1,t2,t3,t4,t5,t11,t6,t7,t8,t9,t10).arrange(DOWN)
    
        # self.add(vg[1])
        # self.add(vg[2])
        # for elem in vg:
            # self.add(elem)
        for i in vg:
            self.play(Write(i))



if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
