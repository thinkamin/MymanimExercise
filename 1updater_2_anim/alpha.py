from manimlib import *
from os import system
import numpy as np

"""

"""

class Test(Scene):
    def construct(self):
        s = Square()
        s.shift(np.array([-2,2,0]))
        self.add(s)
        #这种就像是alpha就像是个常数
        #类似dt
        def myfunc(s,alpha):
            s.move_to(RIGHT*alpha)
            s.rotate(PI*0.05*alpha)

        grid = NumberPlane()
        self.add(grid)
        # updatefromalphafunc 持续run_time时间
        self.play(UpdateFromAlphaFunc(s,myfunc),run_time=9,rate_func=linear)


if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
