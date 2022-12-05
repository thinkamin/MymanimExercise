from manimlib import *
from os import system
import numpy as np

"""

"""

class Test(Scene):
    CONFIG = {
            'ice':'./t1.png',
            'fire':'./t2.png'
            }
    def construct(self):
        ice = ImageMobject(self.ice)
        fire = ImageMobject(self.fire)
        ice.set_height(1)
        fire.set_height(1)
        ice.next_to(fire,LEFT)
        self.play(ShowCreation(ice),run_time=5)
        self.play(ShowCreation(fire),run_time=5)
        


if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
