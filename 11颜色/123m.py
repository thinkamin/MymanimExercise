from manimlib import *
from os import system
import numpy as np
#import matplotlib.pyplot as plt

"""
2022-03-05

"""
'''
颜色表示 
1、（110,0,0）int_RGB
2、（0.2,0.4,0.5）int_RGB
3、#EE001234  hex
4、 WHITE
'''


class Test(Scene):
    def construct(self):
        # grid = NumberPlane()
        # self.add(grid)

        cir = Circle()
        # cir.set_color(RED) = set_stroke
        cir.set_stroke(color=RED,width=15,opacity=0.4)
        cir.set_fill(color=ORANGE,opacity=0.5)
        # self.add(cir)

        rec = Square().set_fill(BLUE,opacity=1).shift(RIGHT*2)
        #
        rec.fade(0.5)
        # self.add(rec)

        #搞不懂
        rec2 = Square()
        rec1 = Square().shift(2*UP).set_fill(BLUE,opacity=1)
        rec3 =Square().set_fill(BLUE,opacity=1)
        vg = VGroup(rec2,rec3).arrange(RIGHT)
        vg.set_gloss(0.5)
        vg.set_shadow(0.8)
        self.add(vg,rec1)
        
        


if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
