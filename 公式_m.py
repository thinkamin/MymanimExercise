from manimlib import *
from os import system
import numpy as np
import itertools as it
#import matplotlib.pyplot as plt

"""
2022-09-07

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

        grid = NumberPlane()
        self.add(grid)
		# string0 = """
		# song yuan long love wan ying ying \n
		# Everyday!!!
		# """
		
        #形状，位置shift，缩放scale，旋转rotate，填充fill，透明度，边框stroke
        #泰勒公式
        talor_name = Text("泰勒公式")
        talor_series = Tex('f(x)=\\frac {f(x_0)} {0!}(x-x_0)+\\frac {f^{''}(x_0)}{2!}(x-x_0)^2+\\dots+\\frac {f^{(n)}(x_0)}{n!}(x-x_0)^n+R_n(x)').scale(0.8)
        talor = VGroup(talor_name,talor_series).arrange(DOWN)
        #螺旋线
        luoxuan_name = Text("螺旋线")
        luoxuan_tex = Tex('x=(\\alpha+\\beta\\theta)cos(\\theta)')
        luoxuan_tex2 = Tex('y=(\\alpha+\\beta\\theta)sin(\\theta)')
        luoxuan = VGroup(luoxuan_name,luoxuan_tex,luoxuan_tex2).arrange(DOWN)
        #三角函数 
        trigle_name = Text("三角函数")
        tri_tex = Tex('cos(\\alpha-\\beta)=cos\\alpha cos\\beta+sin\\alpha sin\\beta')
        tri_tex2 = Tex('cos(\\alpha+\\beta)=cos\\alpha cos\\beta-sin\\alpha sin\\beta')
        tri_tex3 = Tex('sin(\\alpha+\\beta)=sin\\alpha cos\\beta+cos\\alpha sin\\beta')
        tri_tex4 = Tex('sin(\\alpha-\\beta)=sin\\alpha cos\\beta-cos\\alpha sin\\beta')
        tri = VGroup(trigle_name,tri_tex,tri_tex2,tri_tex3,tri_tex4).arrange(DOWN)


        def TexAnim(texlist):
            for vg in texlist:
                self.play(Write(vg))
                self.play(FadeOut(vg))
        texlist = [talor,luoxuan,tri]
        TexAnim(texlist)





if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
