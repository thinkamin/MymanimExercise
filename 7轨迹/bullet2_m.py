from manimlib import *
from os import system
import numpy as np
import itertools as it
#import matplotlib.pyplot as plt

"""
2022-03-13

"""

'''
obj.set_stroke(color=RED,#width=15,opacity=1)
obj.set_fill(color=RED,#opacity=1)
path = TracedPath(obj.get_center,stroke_color=RED,stroke_width=12)
最终结果相关用红色
'''
class Bullet(Triangle):
    CONFIG = {
            "fill_opacity":1,
            "stroke_width":0,
            "length":DEFAULT_ARROW_TIP_LENGTH,
            "start_angle":PI,
            "aspect":1.5,
            "angle":0,
            }
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        digest_config(self,kwargs)
        self.set_height(self.length,stretch=True)
        self.data['points'][4]+=np.array([self.length,0,0])#通过点来改变形状
        self.scale(0.35)

    def get_angle(self):
        return self.angle
    
    def get_vector(self):
        return self.point_from_proportion(0.5)-self.get_start()
    
    def rotate(self,angle,axis=OUT,**kwargs):
        super().rotate(angle,axis,**kwargs)
        self.angle=angle
        return self


class Test(Scene):
    def construct(self):
        #english_font = 'Times New Roman'
        #chinese_font = 'Microsoft YaHei'
        # color_map = it.cycle([BLUE,TEAL,GREEN,YELLOW,GOLD,RED,MAROON,PURPLE])#next(color_map)
        color_map = [BLUE,TEAL,GREEN,YELLOW,GOLD,RED,MAROON,PURPLE]#next(color_map)
        # grid = NumberPlane()
        # self.add(grid)

        trace1 = VGroup()
        trace2 = VGroup()
        trace3 = VGroup()
        def update_one_trace(start_angle):
            def update(obj,dt):
                obj.add(Bullet().rotate(self.time**2*PI+start_angle))
                obj.set_color_by_gradient(*color_map)
                for k in obj:
                    k.shift(np.array([
                        np.cos(k.get_angle()),
                        np.sin(k.get_angle()),
                        0])*4*dt)
                    if abs(get_norm(k.get_center()))>6:
                        obj.remove(k)
            return update
        trace1.add_updater(update_one_trace(0))
        trace2.add_updater(update_one_trace(TAU/3))
        trace3.add_updater(update_one_trace(TAU/3*2))
        self.add(trace1,trace2,trace3)
        self.wait(10)
        




if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
