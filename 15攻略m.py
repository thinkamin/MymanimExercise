from manimlib import *
from os import system
import numpy as np
#import matplotlib.pyplot as plt

"""
2022-02-11

"""

class Test(Scene):
    def construct(self):
        #1实线变虚线
        '''
        c1 = DashedVMobject(Circle(radius=5,color=GREY))
        self.add(c1)
        l1 = DashedVMobject(Line(LEFT*5,color=GREY))
        self.add(l1)
        '''
        #2改变物体颜色 
        '''
        mob = Circle()
        self.add(mob)

        self.play(FadeToColor(mob,GREY))
        '''
        #3围绕 不知道啥用
        '''
        s1 = Square()
        c1 = Circle()
        c1.surround(s1)
        self.add(c1,s1)
        '''
        #4化弧 标注角度使用最多
        '''
        arc = Arc(radius=0.3,arc_center=np.array([-1,0,0]),start_angle=0,angle=30*DEGREES)

        self.play(ShowCreation(arc))
        '''
        #5rotate Rotating
        #Rotating:每一帧都会创建一个target
        #rotate:只生成一个target，中间直接补间动画
        '''
        s1 = Ellipse()
        s2 = Square()
        self.add(s1,s2)
        self.play(Rotating(s1,axis=IN,radians=PI))
        '''
        #7MoveToTarget
        '''
        a = Text('text')
        #先复制自己成为a的target数形
        a.generate_target()
        #使target变成Square
        a.target.become(Square(side_length=2,color=BLUE).shift(RIGHT*2))
        self.add(a)
        self.play(MoveToTarget(a),run_time=5)
        '''
        # 9become 使用become不会改变前一个对象
        '''
        c1=Circle()
        s1=Square(side_length=2)
        self.add(c1,s1)
        self.play(c1.become,s1,run_time=5)
        '''
        #10删除文字
        '''
        text = Text('abcdefg')
        # self.add(text)
        self.play(Write(text))
        self.play(Uncreate(text),run_time=3)
        '''



if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
