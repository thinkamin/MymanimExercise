from manimlib import *
from os import system
import numpy as np
#import matplotlib.pyplot as plt

"""
2022-02-08

"""

class Test(Scene):
    def construct(self):

        grid = NumberPlane()
        self.add(grid)
        tex = Tex('f(x)=\\frac {a_0}{2} +\\sum_{n=0}^\\infty a_n cosnx +\\sum_{n=0}^\\infty b_n sinnx')
        self.add(tex)
        tex2 = Tex('e^{i\\pi}+1=0')
        tex2.shift(DOWN)
        self.add(tex2)



if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
