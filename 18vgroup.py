from manimlib import *
from os import system
import numpy as np

"""
2021-12-14

"""

class Test(Scene):
    @staticmethod
    def Build_numbers() :
        lines = []
        for line_num in range(1, 4) :
            line = []
            mystr = lambda x: 'n' if x==1 else str(x)+'n'
            for col_num in range(1, 4) :
                line.append(Tex(str(line_num*col_num)))
            line.append(Tex('\\cdots'))
            line.append(Tex(mystr(line_num)))
            lines.append(line)
        lines.append([Tex('\\vdots'), Tex('\\vdots'), Tex('\\vdots'), Tex('\\ddots'), Tex('\\vdots')])
        lines.append([Tex('n'), Tex('2n'), Tex('3n'), Tex('\\cdots'), Tex('n^2')])
        return lines

    def construct(self):
        lines = self.Build_numbers()
        lines_group_list = [VGroup(*lines[0]).arrange(buff=1).to_edge(UP)]
        for line_num in range(1, 5) :
            for col_num in range(5) :
                lines[line_num][col_num].move_to(lines[line_num-1][col_num].get_center()+DOWN)
            lines_group_list.append(VGroup(*lines[line_num]))
        lines_group = VGroup(*lines_group_list)

        col_group_list = []
        for col_num in range(5) :
            col_list = []
            for line_num in range(5) :
                col_list.append(lines[line_num][col_num])
            col_group_list.append(VGroup(*col_list))
        col_group = VGroup(*col_group_list)

        all = lines_group
        all.move_to(ORIGIN)
        for line in range(5) :
            self.play(Write(lines_group_list[line]))
        self.wait(2)
        


if __name__=="__main__":
   system('manimgl {}'.format(__file__)) 
