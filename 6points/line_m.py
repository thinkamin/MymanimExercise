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

        line = Circle()
        #增加4段曲线 12个点
        line.insert_n_curves(4)
        # print(line.get_num_points())
        self.add(line)

        # self.play(ApplyPointwiseFunction(np.exp,line),run_time=6)




if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
