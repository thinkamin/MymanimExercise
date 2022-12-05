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

        dot = Dot(LEFT*3+DOWN*2)
        text = Text('This is some text').next_to(dot,RIGHT)
        envelop = VGroup()
        text.add_updater(lambda a:a.next_to(dot,RIGHT))
        
        def stamp(obj):
            obj.add(text.copy().clear_updaters().set_opacity(0.2))

        envelop.add_updater(stamp)
        self.add(dot,text,envelop)
        self.play(dot.shift,UP*4,rate_func=there_and_back,run_time=4)



if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
