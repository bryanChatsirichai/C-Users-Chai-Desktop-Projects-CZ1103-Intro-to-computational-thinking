from sense_hat import SenseHat

sense = SenseHat()
import time
import random

r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
y = (255, 255, 0)
p = (255, 0, 255)
colour = [r, g, y]
degree = [0, 90, 180, 270]


def rot():
    return random.choice(degree)


def col():
    return random.choice(colour)


while True:
    image_pixel = [b, b, b, b, b, b, b, b,
                  b, b, b, col(), b, b, b, b,
                  b, b, col(), col(), col(), b, b, b,
                  b, col(), b, col(), b, col(), b, b,
                  b, b, b, col(), b, b, b, b,
                  b, b, b, b, col(), b, b, b,
                  b, b, b, col(), b, b, b, b,
                  b, b, b, b, b, b, b, b]
    sense.set_rotation(rot())
    sense.set_pixels(image_pixel)
    time.sleep(1)
    sense.clear()
