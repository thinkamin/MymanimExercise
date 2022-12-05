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
        dot0 = Dot(RIGHT*2)
        cir0=Circle(radius=1.5,color=YELLOW)
        dotp=Dot()
        cirp=Circle()
        enve = VGroup()
        self.i=0
        def anim(obj,alpha):
            obj.move_to(cir0.point_from_proportion(alpha))

        def anim_cir(obj):
            obj.become(Circle(radius=abs(get_norm(dot0.get_center()-dotp.get_center())))).move_to(dotp.get_center())

        cirp.add_updater(anim_cir)

        def stamp(obj):
            if self.i%6==0:
                obj.add(cirp.copy().clear_updaters().set_stroke(color=PURPLE,width=1))
            self.i+=1
        enve.add_updater(stamp)
        self.add(cir0,dot0,dotp,enve)
        self.play(UpdateFromAlphaFunc(dotp,anim),run_time=10)
        





if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
