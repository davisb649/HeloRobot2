import gopigo
import time
class Piggy(object):

    def __init__(self):
        print("I live")

    def cha_cha(self):
        for x in range(5):
            right_rot()
            time.sleep(.5)
            left_rot()
            time.sleep(.5)
            stop()

p = Piggy()
p.cha_cha()