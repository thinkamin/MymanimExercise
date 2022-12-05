#import  gen_num
# num_lst = gen_num.gen_num1(10)
# print(num_lst)
from manimlib import *
import numpy as np
class Test(Scene):
    def construct(self):
        s = Square(fill_color=RED,fill_opacity=0.5)
        p = Square(fill_color=RED,fill_opacity=0.5).get_grid(2,2,height=5)
        # s.fill_data('9')
        # s.set_fill(RED)
        # s.set_color_by_gradient(GREEN,RED)
        s.rotate(np.pi/3)
        s.shift(UP)
        self.add(s)

        self.play(s.animate.shift(LEFT))
        self.play(s.animate.rotate(np.pi/3))
        self.play(s.animate.set_opacity(1))
        self.play(s.animate.set_opacity(1))
        #全部
        self.play(s.animate.set_color(GREEN))
        #中间
        self.play(s.animate.set_fill(WHITE))
        #边
        self.play(s.animate.set_stroke(GREEN,5))

        #针对gird    
        self.play(p.animate.set_submobject_colors_by_gradient(BLUE,GREEN))
        #放大
        self.play(p.animate.set_height(TAU-MED_SMALL_BUFF))
        #应用复函数
        self.play(p.animate.apply_complex_function(np.exp),run_time=5)
        #应用一般函数 lamba p :
        self.play(s.animate.apply_function(lambda p:[p[0]+0.5*math.sin(p[1]),
             p[1]+0.5*math.sin(p[0]),
             p[2]]))
        
    
        

