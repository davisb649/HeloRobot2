from gopigo import *
import time
class Piggy(object):

    def __init__(self):
        print("I live")

    def cha_cha(self):
        for x in range(5):
            right_rot()
            time.sleep(.5)
            fwd()
            time.sleep(1)
            left_rot()
            time.sleep(.5)
            bwd()
            time.sleep(1)
            stop()

p = Piggy()
p.cha_cha()