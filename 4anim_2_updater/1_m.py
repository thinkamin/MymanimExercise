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

        s1 = Square()
        anim = FadeIn(s1,rate_func=there_and_back,run_time=3)
        turn_animation_into_updater(anim,True)#True：循环播放 False：不循环播放
        s1.add_updater(lambda m,dt:m.shift(10*UP*dt))#??
        # self.play(anim,run_time=4)
        self.add(s1)
        self.wait(6)#循环2编
        s1.clear_updaters()


        self.add(s1)
        s1.add_updater(lambda a,dt:a.rotate(20*DEGREES*dt))#??
        self.wait()


if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
