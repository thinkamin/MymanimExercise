from manimlib import *
from os import system
import numpy as np


class Arrange01(Scene):
    def construct(self):
        square1,square2 = VGroup(
            Square(color=RED),
            Square(color=BLUE)
        ).scale(0.5).set_x(-5)

        reference = DashedVMobject(Line(LEFT*5,RIGHT*5,color=WHITE))
        self.add(square1,square2,reference)

        square2.save_state()
        def update_rotate_move(mob,alpha):
            square2.restore()
            mob.shift(5*RIGHT*alpha)
            mob.rotate(TAU*alpha)

        self.play(
            UpdateFromAlphaFunc(square2,update_rotate_move),
            run_time=6
        )

if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
