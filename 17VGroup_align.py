from manimlib import *
from os import system
import numpy as np

"""
2021-12-13

"""

class Test(Scene):
    def construct(self):
        unit = 0.4
        sq = VGroup()
        sq.add(Square(side_length=unit).move_to(np.array([-5.2,2.6,0])))
        for num in range(2,6):
            sq.add(VGroup(
                *[
                    Square(side_length=unit*num)
                    for i in range(num)
                    ]
                ).arrange(RIGHT,buff=0).next_to(sq[-1],DOWN,aligned_edge=LEFT,buff=0))
        self.add(sq)
        # self.play(ShowCreation(sq[0]))

if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
