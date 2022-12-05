from manimlib import *
from os import system
import numpy as np
#import matplotlib.pyplot as plt

"""
2022-03-03

"""

class Test(Scene):
    def construct(self):

        grid = NumberPlane()
        self.add(grid)
        
        s1 = Square().shift(LEFT*3)
        s1.save_state()

        def anim(obj,alpha):
            obj.restore()
            obj.shift(6*RIGHT*alpha)#6*RIGHT就决定了终点
            obj.rotate(TAU*alpha)#期间旋转一个2pi
        self.play(UpdateFromAlphaFunc(s1,anim),run_time=10)



if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
