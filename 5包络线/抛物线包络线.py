from manimlib import *
from os import system
import numpy as np
#import matplotlib.pyplot as plt

"""
2022-03-04

"""

class Test(Scene):
    def construct(self):

        grid = NumberPlane()
        self.add(grid)

        line = Line(LEFT*7,RIGHT*7).shift(UP*3)
        dotF=Dot(UP)
        dotP=Dot(color=ORANGE)
        l_fp=Line()
        l_h=Line()
        enve = VGroup()
        self.i=0

        def anim(obj,alpha):
            obj.move_to(line.point_from_proportion(alpha))

        def anim_line(obj):
            obj.put_start_and_end_on(dotP.get_center(),dotF.get_center())

        l_fp.add_updater(anim_line)

        def anim_line2(obj):
            obj.become(l_fp.copy().set_color(BLUE).rotate(PI/2)).scale(20)

        l_h.add_updater(anim_line2)
        
        def stamp(obj):
            if self.i%6==0:
                #动直线复制 同时删掉updaters 设置笔刷大小 颜色等
                obj.add(l_h.copy().clear_updaters().set_stroke(width=1))
            self.i+=1

        enve.add_updater(stamp)
        self.add(line,dotF,dotP,l_fp,l_h,enve)
        self.play(UpdateFromAlphaFunc(dotP,anim),run_time=10)



if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
