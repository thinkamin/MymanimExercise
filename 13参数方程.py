from manimlib import *
import numpy as np

"""

"""

class Test(Scene):
    def construct(self):

        '''
        func = FunctionGraph(
                lambda x:x**2
                )
        self.play(ShowCreation(func))

        '''
        t_range=(0,2*PI)
        func2 = ParametricCurve(
                lambda t:np.array([
                    2*np.sin(3*t)*np.cos(t),
                    2*np.sin(3*t)*np.sin(t),
                    0
                    ]),t_range
                )
        self.play(ShowCreation(func2))
        func4 = ParametricCurve(
                lambda t:np.array([
                    2*np.cos(t),
                    2*np.sin(t),
                    0
                    ]),t_range
                )
        
        self.play(ShowCreation(func4))
        
