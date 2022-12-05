from manimlib import *
from os import system
import numpy as np
#import matplotlib.pyplot as plt

"""
2022-03-05

"""

class Test(Scene):
    def construct(self):

        grid = NumberPlane()
        self.add(grid)

        cir = Circle()
        self.add(cir)

        #这个可以实现对每个xyz的操作
        self.play(cir.animate.apply_function(lambda p:[2*p[0],3*p[1],p[2]]))


        def point_f(p):
            return p[0]*2,p[1]*2,p[2]

        # self.play(ApplyPointwiseFunction(np.sin,cir))
        self.play(ApplyPointwiseFunction(point_f,cir))
        self.play(ApplyMatrix([[0,1],[1,0]],cir))


        



if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
