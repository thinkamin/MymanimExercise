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

        t = ValueTracker(0)
        cir = Circle(radius=2).shift(LEFT*5)
        dot_o=Dot(LEFT*5)
        dot_a=Dot(LEFT*3)
        l_oa = Line(LEFT*5,LEFT*3)
        dot_p = Dot().add_updater(lambda a:a.move_to(
            np.array([
                -5+2*np.cos(t.get_value()),#-5+2cost
                2*np.sin(t.get_value()),#2sint
                0
                ])
            ))
        l_op = Line().add_updater(lambda a:a.put_start_and_end_on(
            dot_o.get_center(),
            dot_p.get_center()
            ))
        arc = Arc(angle=0).add_updater(lambda a:a.become(Arc(start_angle=0,angle_end=t.get_value())))

        dot_q=Dot().add_updater(lambda a:a.move_to(
            np.array([
                0,
                2*np.sin(t.get_value()),
                0
                ])
            ))

        l_pq= Line().add_updater(lambda a:a.put_start_and_end_on(
            dot_p.get_center(),
            dot_q.get_center()
            ))
        # dt = 1/self.camera.frame_rate
        path = TracingTail(dot_q.get_center,stroke_width=6,stroke_color=YELLOW)
        # def path_anim(obj,alpha):
            # obj.shift(SHIFT*alpha)
        path.add_updater(lambda a,dt:a.shift(RIGHT*dt))

        self.add(cir,dot_o,dot_p,dot_a,l_oa,l_op,dot_q,l_pq,path)
        self.play(t.set_value,2*TAU,run_time=8)
        # self.play(t.set_value(2*TAU))



if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
