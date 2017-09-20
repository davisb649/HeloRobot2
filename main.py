from gopigo import *
import time
class Piggy(object):

    def __init__(self):
        print("I live")

    def pulse(self):
        """check for obstacles, drive fixed amount fwd"""
        look = us_dist(15)  # store the dist reading
        if look > 80:
            fwd()
            time.sleep(1)
            stop()

    def cruise(self):
        """drive fwd, stop if sensor detects obstacle"""
        fwd()
        while(True):
            if us_dist(15) < 30:
                stop()
            time.sleep(.2)

    def servo_sweep(self):
        """loops in a 120 deg arc and moves servo"""
        for ang in range(20, 160, 2):
            servo(ang)
            time.sleep(.2)

    def cha_cha(self):
        for x in range(3):
            right_rot()
            time.sleep(.25)
            fwd()
            time.sleep(1)
            left_rot()
            time.sleep(.25)
            bwd()
            time.sleep(1)
            stop()

p = Piggy()
