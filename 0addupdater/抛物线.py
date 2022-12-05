from manimlib import *
from os import system
import numpy as np
#import matplotlib.pyplot as plt

"""
2022-02-21

"""

class Test(Scene):
    def construct(self):
        grid = NumberPlane()
        self.add(grid)
        t = ValueTracker(-1)
        # obj = Ellipse(width=10,height=6)
        p=2
        dot_f1 = Dot(LEFT*4)
        dot_f2 = Dot(RIGHT*4)
        dot_p = Dot(color=RED).add_updater(lambda a:a.move_to(np.array([
            2*p*(t.get_value()**2),
            2*p*(t.get_value()),
            0
            ])))
        l_f1p = Line().add_updater(lambda a:a.put_start_and_end_on(
            dot_f1.get_center(),
            dot_p.get_center()
            ))
        l_f2p = Line().add_updater(lambda a:a.put_start_and_end_on(
            dot_f2.get_center(),
            dot_p.get_center()
            ))
        self.add(dot_f1,dot_f2,dot_p,l_f1p,l_f2p)
        path = TracedPath(dot_p.get_center)
        self.add(path)
        
        self.play(t.set_value,1,run_time=9)





if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
