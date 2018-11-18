#!/usr/bin/env python3
from ev3dev.ev3 import *

ml = LargeMotor("outA")
mr = LargeMotor("outB")
mm = MediumMotor("outC")
ml.reset()
mr.reset()
mm.reset()

#          0 = up
#3 = left          1 = right
#          2 = down
rotrob = 0

#0 = nevi
#1 = block
#2 = nic neprojeto
#3 = nic projeto
#4 = robot

pole = [[0,1,2,3,4,5,6,7,8],
        [0,1,2,3,4,5,6,7,8],
        [0,1,2,3,4,5,6,7,8],
        [0,1,2,3,4,5,6,7,8],
        [0,1,2,3,4,5,6,7,8],
        [0,1,2,3,4,5,6,7,8]]

def forw():
        ml.run_to_rel_pos(speed_sp = 500, position_sp = 360, stop_action = "hold")
        mr.run_to_rel_pos(speed_sp = 500, position_sp = 360, stop_action = "hold")

def left():
        ml.run_to_rel_pos(speed_sp = 500, position_sp = -360, stop_action = "hold")
        mr.run_to_rel_pos(speed_sp = 500, position_sp = 360, stop_action = "hold")

def right():
        ml.run_to_rel_pos(speed_sp = 500, position_sp = 360, stop_action = "hold")
        mr.run_to_rel_pos(speed_sp = 500, position_sp = -360, stop_action = "hold")

def back():
        ml.run_to_rel_pos(speed_sp = 500, position_sp = -360, stop_action = "hold")
        mr.run_to_rel_pos(speed_sp = 500, position_sp = -360, stop_action = "hold")


