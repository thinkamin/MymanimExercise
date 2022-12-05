from manimlib import *
from os import system
import numpy as np
import itertools as it
#import matplotlib.pyplot as plt

"""
2022-03-19

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
        t0 = Tex('f(x)=a_0+a_1x+a_2x^2+a_3x^3+\\dots+a_nx^n+\\dots')
        t1 = Tex('x=0')
        t2 = Tex('f(0)=a_0')
        t3 = Tex("f^{'}(x)=a_1+2a_2x+3a_3x^3+\\dots+na_nx^(n-1)+\\dots")
        t4 = Tex("f^{'}(0)=a_1")
        t5 = Tex("f^{''}(x)=1\\cdot 2 a_2+2\\cdot 3 a_3x^2+\\dots+(n-1) \\cdot na_nx^(n-2)+\\dots")
        t6 = Tex("f^{''}(0)=2!a_2")
        vg = VGroup(t0,t1,t2,t3,t4,t5,t6).arrange(DOWN)
        self.add(vg)




if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
