#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

ultra = UltrasonicSensor()

ml = LargeMotor("outA")
mr = LargeMotor("outB")
mm = MediumMotor("outC")
ml.reset()
mr.reset()
mm.reset()

ultrapos = 0

turn = False

forwa = 0
lef = 0
righ = 0

#          0 = forw
#3 = left            1 = right
#          2 = back
rotrob = 0
posrob = [3,4]

#0 = nevi
#1 = block
#2 = nic neprojeto
#3 = nic projeto
#4 = robot

pole = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,1,3,1,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]


#movement
def forw():
        ml.run_to_rel_pos(speed_sp = 500, position_sp = 5, stop_action = "hold")
        mr.run_to_rel_pos(speed_sp = 500, position_sp = 5, stop_action = "hold")

def left():
        ml.run_to_rel_pos(speed_sp = 200, position_sp = -2, stop_action = "hold")
        mr.run_to_rel_pos(speed_sp = 200, position_sp = 2, stop_action = "hold")

def right():
        ml.run_to_rel_pos(speed_sp = 200, position_sp = 2, stop_action = "hold")
        mr.run_to_rel_pos(speed_sp = 200, position_sp = -2, stop_action = "hold")

def back():
        ml.run_to_rel_pos(speed_sp = 500, position_sp = -360, stop_action = "hold")
        mr.run_to_rel_pos(speed_sp = 500, position_sp = -360, stop_action = "hold")


#sensor
def ultraread(side,ultrapos):
        if side == 0:
                mm.run_to_rel_pos(speed_sp = 200, position_sp = (ultrapos)*-1)
                mm.wait_until_not_moving()
                ultrapos = (ultrapos)*-1
                return ultra.distance_centimeters()
        elif side == 1:
                mm.run_to_rel_pos(speed_sp = 200, position_sp = (90+ultrapos)*-1)
                mm.wait_until_not_moving()
                ultrapos = (90+ultrapos)*-1
                return ultra.distance_centimeters()
        elif side == 3:
                mm.run_to_rel_pos(speed_sp = 200, position_sp = 90+(ultrapos*-1))
                mm.wait_until_not_moving()
                ultrapos = 90+(ultrapos*-1)
                return ultra.distance_centimeters()


def mapupdate(position, direction, forw, right, left):
        if direction == 0:
                for x in range(forw):
                        pole[position[0]-x-1][position[1]] = 2
                pole[position[0]-forw-1][position[1]] = 1
                for x in range(left):
                        pole[position[0]][position[1]-x-1] = 2
                pole[position[0]][position[1]-left-1] = 1
        




while True:
        turn = True
        vzdalen = 0
        forwa = ultraread(0,ultrapos)
        righ = ultraread(1,ultrapos)
        lef = ultraread(3,ultrapos)

        if forw > right and forw > left:
                while ultraread(0,ultrapos) < 8:
                        forw()
        elif right > forw and right > left:
                while turn:
                        vzdalen = ultraread(0,ultrapos)
                        sleep(0.1)
                        if ultraread(0,ultrapos) < vzdalen:
                                right()
                        else:
                                turn = False
        elif left > forw and left > right:
                while turn:
                        vzdalen = ultraread(0,ultrapos)
                        sleep(0.1)
                        if ultraread(0,ultrapos) < vzdalen:
                                left()
                        else:
                                turn = False

