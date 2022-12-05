from manimlib import *
from os import system
import numpy as np

class Test(Scene):
    def construct(self):
        #划线
        def put_line_on(a,b):
            def update(line):
                line.put_start_and_end_on(a.get_center(),b.get_center())
            return update
        #更新点 （目标点-当前点)*dt
        def update_dot(target):
            def anim(obj,dt):
                obj.shift((target.get_center()-obj.get_center())*dt)
            return anim
        dot_a = Dot(np.array([2,2,0]))
        dot_b = Dot(np.array([2,-2,0]))
        dot_c = Dot(np.array([-2,-2,0]))
        dot_d = Dot(np.array([-2,2,0]))
        dot_a.add_updater(update_dot(dot_b))
        dot_b.add_updater(update_dot(dot_c))
        dot_c.add_updater(update_dot(dot_d))
        dot_d.add_updater(update_dot(dot_a))
        self.add(dot_a,dot_b,dot_c,dot_d)
        # self.wait(5)
        l_ab = Line(dot_a,dot_b)
        l_bc = Line(dot_b,dot_c)
        l_cd = Line(dot_c,dot_d)
        l_da = Line(dot_d,dot_a)
        self.add(l_ab,l_bc,l_cd,l_da)
        l_ab.add_updater(put_line_on(dot_a,dot_b))
        l_bc.add_updater(put_line_on(dot_b,dot_c))
        l_cd.add_updater(put_line_on(dot_c,dot_d))
        l_da.add_updater(put_line_on(dot_d,dot_a))
        trace = VGroup()
        trace.add_updater(lambda a,dt:#间隔dt采样一次并add到达印章效果
                a.add(
                    l_ab.copy().clear_updaters().set_stroke(width=0.6),
                    l_bc.copy().clear_updaters().set_stroke(width=0.6),
                    l_cd.copy().clear_updaters().set_stroke(width=0.6),
                    l_da.copy().clear_updaters().set_stroke(width=0.6),
                    ))
        self.add(trace)
        self.wait(5)
        


if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
