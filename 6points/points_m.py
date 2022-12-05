from manimlib import *
from os import system
import numpy as np
#import matplotlib.pyplot as plt

"""
2022-03-03

"""

class Test(Scene):
    def construct(self):

        grid = NumberPlane()
        self.add(grid)
        l_oa = Line().shift(UR*3)
        self.add(l_oa)
        points = l_oa.get_all_points()
        self.show_points(self,points)
        #边界点 选择每段贝塞尔曲线的中间那个
        boundary_point = Dot(l_oa.get_boundary_point(UP)).set_color(BLUE)
        self.add(boundary_point)
        #打印len（get_all_points)
        print(l_oa.get_num_points())


        cir = Circle().shift(LEFT*3).scale(2)
        self.add(cir)
        points = cir.get_all_points()
        self.show_points(self,points)
        # self.play(ApplyPointwiseFunction(np.exp,cir))
        matrix = [[1,2],
                 [2,1]]
        self.play(ApplyMatrix(matrix,cir))
        # self.add(cir.get_bounding_box())

        boundary_point = Dot(cir.get_boundary_point(UP)).set_color(BLUE)
        self.add(boundary_point)
        # self.play(cir.apply_points_function(lambda x:x**2))

        sq = Square().shift(DR)
        self.add(sq)
        points = sq.get_all_points()
        self.show_points(self,points)

        boundary_point = Dot(sq.get_boundary_point(UP)).set_color(BLUE)
        self.add(boundary_point)
    @staticmethod
    def show_points(self,obj):
        for point in obj:
            self.add(Dot(point,color=RED))



if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
