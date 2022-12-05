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
        
        s1 = Square(side_length=2)
        def anim(obj):
            obj.shift(RIGHT*0.01)
            obj.rotate(0.01*TAU)
        self.play(UpdateFromFunc(s1,anim,run_time=10))
        print(s1.get_center())
        #这个也能实现边走边转，
        #但是不像那样alpha有起始点
        #也不像dt对每一帧画面进行控制,可以很精准
        



if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
