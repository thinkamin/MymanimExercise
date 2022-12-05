from manimlib import *
from os import system
import numpy as np
import itertools as it
#import matplotlib.pyplot as plt

"""
2022-03-26

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
        chinese_font = 'Microsoft YaHei'
        #color_map = it.cycle(BLUE,TEAL,GREEN,YELLOW,GOLD,RED,MAROON,PURPLE)#next(color_map)
        def point2dot_tex(point,a,position=UP,color=WHITE):
            dot = Dot(point).set_fill(color)
            t = Tex(a).next_to(dot,position)
            self.play(ShowCreation(dot),Write(t))
        def draw_line(point1,point2):
            line = Line(point1,point2,color=RED)
            self.play(ShowCreation(line))
        def showstr(string,position=2.7*DOWN,font=chinese_font):
            text = Text(string,font=chinese_font).shift(position)
            self.play(FadeIn(text))
            self.wait(1)
            self.play(FadeOut(text))

        s1='1、微分方程:联系自变量、未知函数及其导数的关系式'
        s2='2、常微分方程:只有一个自变量的微分方程'
        s3='3、偏微分方程:有两个或两个以上自变量的微分方程'
        s4='4、一阶微分方程:微分方程中未知函数的导数仅为一阶'
        s5='5、n阶微分方程:'
        t5=Tex('F(x,y,\\frac{dy}{dx},\\dots,\\frac{d^n y}{dx^n})=0')
        # self.play(Write(t5))
        s6='6、n阶线性微分方程:'
        t6=Tex('\\frac{d^n y}{dx^n}+a_1(x)\\frac{d^{n-1}}{dx^{n-1}}+\\dots+a_{n-1}(x)\\frac{dy}{dx}+a_n(x)y=f(x)')
        self.play(Write(t6))
        s7='一阶一次常微分方程'
        t7=Tex('\\frac {dx}{dt}+kx=ka')
        s8='二阶一次常微分方程'
        t8=Tex('m\\frac {d^2x}{dt^2}+v\\frac{dx}{dt}+kx=0')



if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
