from manimlib import *
# from manimlib.utils.calculation import get_intersect#想办法解决
from os import system
import numpy as np

"""
2022-03-05

"""

class Test(Scene):
    def construct(self):

        grid = NumberPlane()
        self.add(grid)

        l1= Line(LEFT*2,UR*1).scale(2)
        l2= Line(RIGHT*2,UR*1).scale(2)
        self.add(l1,l2)

        # l1,l2 不能为0 或90度
        dot = Dot().add_updater(lambda m:m.move_to(get_intersect_ll(l1,l2,LEFT*100)))
        self.add(dot)

        l3 = Line().rotate(PI/6).shift(RIGHT*0.5)
        cir = Circle()
        self.add(l3,cir)
        #l3 不能为0 或90度
        point_a,point_b = get_intersect_lc(l3,cir)
        # print(point_a,point_b)
        dot_a,dot_b = Dot(point_a),Dot(point_b)
        t1 = Tex('A').next_to(dot_a)
        t2 = Tex('B').next_to(dot_b)
        self.add(dot_a,dot_b)
        self.add(t1,t2)




if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
