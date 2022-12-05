from manimlib import *
from os import system
import numpy as np
import itertools as it
#import matplotlib.pyplot as plt

"""
2022-04-09

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
        def showstr(string,position=2.7*DOWN,font=chinese_font):
            text = Text(string,font=chinese_font,color=RED).shift(position)
            self.play(FadeIn(text))
            self.wait(1)
            self.play(FadeOut(text))
        vg = self.show_question()
        self.add(vg)
        self.wait(3)
        self.play(vg.animate.move_to(2*UR).scale(0.8))
        self.play(FadeOut(vg[2]))
        analize1 = '第一问比较简单，求导 讨论a的不同取值范围 即可'
        showstr(analize1)
        Q1_0=Tex("f^{'}(x)=-\\frac{1}{x^2}-1+\\frac{a}{x}")
        Q1_0.set_color_by_gradient(GREEN,RED)
        Q1_1=Tex('=-\\frac{1+x^2-ax}{x^2}')
        Q1_2=Tex("\\Delta = a^2-4")
        vg1 = VGroup(Q1_0,Q1_1,Q1_2).move_to(2*DOWN).arrange(DOWN)
        self.play(Write(vg1))
        self.wait(2)
        self.play(FadeOut(vg1))
        self.play(FadeOut(vg[1]),FadeIn(vg[2]))
        analize2 = '第二问就稍微有点复杂，是一个x1,x2，a的三元关系式'
        showstr(analize2)
        analize3 = '考虑边形 消元'
        showstr(analize3)
        t2_0=Tex('f(x_1)-f(x_2)>(a-2)(x_1-x_2)')
        t2_0_1=Tex('\\frac{1}{x_1}-\\frac{1}{x_2}-(x_1-x_2)+a(lnx_1-lnx_2)-(a-2)(x_1-x_2)>0')
        t2_0_2=Tex('\\frac{x_2-x_1}{x_1x_2}-(x_1-x_2)+aln(x_1/x_2)-(a-2)(x_1-x_2)>0')
        self.play(Write(t2_0))
        self.play(FadeOut(t2_0))
        self.play(Write(t2_0_1))
        self.play(FadeOut(t2_0_1))
        self.play(Write(t2_0_2))
        self.play(t2_0_2.animate.move_to(RIGHT).scale(0.8))
        # self.play(FadeOut(t2_0))
        t2_1=Text("因为x1,x2满足f'(x)=0,所以满足以下等式")
        t2_2=Tex('x_1^2-ax_1+1=0')
        t2_3=Tex('x_2^2-ax_2+1=0')
        t2_4=Tex('x_1+x_2=a')
        t2_5=Tex('x_1x_2=1')
        t2_6=Tex('x_1=\\frac{a-\\sqrt{a^2-4}}{2}')
        t2_7=Tex('x_2=\\frac{a+\\sqrt{a^2-4}}{2}')
        vg2=VGroup(t2_1,t2_2,t2_3,t2_4,t2_5,t2_6,t2_7).arrange(DOWN).move_to(2*2*LEFT).scale(0.5)
        self.play(Write(vg2))
        t3_1=Text('把x1x2=1代入')
        t3_2=Tex('-(x_1-x_2)+aln(x_1/x_2)-(a-1)(x_1-x_2)>0')
        analize4='这里就要考虑直接将x1x2全部消掉还是消掉一个？'
        showstr(analize4)


         

    def show_question(self):
        t1 = Tex('f(x)=\\frac 1 x -x+alnx')
        text1=Text('1、讨论单调性')
        Q1=VGroup(text1)
        text2=Text('2、f(x)存在两个极致点x1,x2,证明：')
        t2=Tex('\\frac {f(x_1)-f(x_2)}{x_1-x_2}<a-2')
        Q2=VGroup(text2,t2).arrange(DOWN)
        vg = VGroup(t1,Q1,Q2).arrange(DOWN)
        return vg





if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
