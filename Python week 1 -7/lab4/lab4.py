from sense_hat import SenseHat
sense = SenseHat()
import time
import random
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
purple = (255,0,255)
def rdm():
    return random.randint(0,7)

sense.clear()
while True:

    sense.set_pixel(rdm(),rdm(),red)
    time.sleep(1)
    sense.clear()

    sense.set_pixel(rdm(),rdm(),green)
    time.sleep(1)
    sense.clear()

    sense.set_pixel(rdm(),rdm(),blue)
    time.sleep(1)
    sense.clear()

    sense.set_pixel(rdm(),rdm(),purple)
    time.sleep(1)
    sense.clear()
