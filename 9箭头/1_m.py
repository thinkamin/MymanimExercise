from manimlib import *
from os import system
import numpy as np
#import matplotlib.pyplot as plt

"""
2022-03-07

"""

'''
obj.set_stroke(color=RED,#width=15,opacity=1)
obj.set_fill(color=RED,#opacity=1)
path = TracedPath(obj.get_center,stroke_color=RED,stroke_width=12)
'''
class Test(Scene):
    def construct(self):
        #english_font = 'Times New Roman'
        #chinese_font = 'Microsoft YaHei'

        # grid = NumberPlane()
        # self.add(grid)

        a = NumberLine()
        self.add(a)
        tex1 = Tex('1\\times(-1)=-1').shift(UP*2)
        self.play(Write(tex1))
        vec1 = Vector()
        self.add(vec1)

        point_a = np.array([1,0,0])
        point_b = np.array([-1,0,0])

        c = CurvedArrow(point_a,point_b,angle=PI)
        self.play(Rotate(vec1,PI,about_point=ORIGIN),ShowCreation(c),run_time=5)
        self.play(FadeOut(c),FadeOut(a),FadeOut(vec1),FadeOut(tex1))
        # b = CoordinateSystem()
        # self.add(b)
        axes = Axes(
                x_range=[-1.5,1.5],
                y_range=[-1.5,1.5],
                height=4,
                width=4,
                )
        axes.add_coordinate_labels(
                font_size=20,
                num_decimal_places=1,
                )
        self.play(ShowCreation(axes))

        point_a = np.array([1,0,0])
        point_b = np.array([0,1,0])
        point_c = np.array([-1,0,0])

        d = CurvedArrow(point_a,point_b,angle=PI/2)
        f = CurvedArrow(point_b,point_c ,angle=PI/2)

        self.play(ShowCreation(d))
        tex2 = Tex('1\\times i =i').next_to(d,RIGHT)
        self.play(ShowCreation(tex2))

        self.play(ShowCreation(f))
        tex3 = Tex('i\\times i=-1').next_to(f,LEFT)
        self.play(ShowCreation(tex3))
        





if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
