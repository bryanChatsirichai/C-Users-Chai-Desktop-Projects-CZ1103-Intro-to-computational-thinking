from sense_hat import SenseHat
sense = SenseHat()
import time
import random
r = (255,0,0)
g = (0,255,0)
b= (0,0,255)
y = (255,255,0)
p = (255,0,255)
colour = [r,g,y]
choose = random.choice(colour)
sense.clear()
def col():
    return random.choice(colour)


image_pixels_top =         [col(), col(), col(),col(), col(), col(), col(),col(),
                            b, b, b, b, b, b, b, b,
                            b, b, b, b, b, b, b, b,
                            b, b, b, b, b, b, b, b,
                            b, b, b, b, b, b, b, b,
                            b, b, b, b, b, b, b, b,
                            b, b, b, b, b, b, b, b,
                            b, b, b, b, b, b, b, b]
  
image_pixels_right =       [b, b, b, b, b, b, b, col(),
                            b, b, b, b, b, b, b, col(),
                            b, b, b, b, b, b, b, col(),
                            b, b, b, b, b, b, b, col(),
                            b, b, b, b, b, b, b, col(),
                            b, b, b, b, b, b, b, col(),
                            b, b, b, b, b, b, b, col(),
                            b, b, b, b, b, b, b, col()]
                            
image_pixels_bot =         [b, b, b, b, b, b, b, b,
                            b, b, b, b, b, b, b, b,
                            b, b, b, b, b, b, b, b,
                            b, b, b, b, b, b, b, b,
                            b, b, b, b, b, b, b, b,
                            b, b, b, b, b, b, b, b,
                            b, b, b, b, b, b, b, b,
                            col(), col(), col(), col(), col(), col(), col(), col()]
        
image_pixels_left =        [col(), b, b, b, b, b, b, b,
                            col(), b, b, b, b, b, b, b,
                            col(), b, b, b, b, b, b, b,
                            col(), b, b, b, b, b, b, b,
                            col(), b, b, b, b, b, b, b,
                            col(), b, b, b, b, b, b, b,
                            col(), b, b, b, b, b, b, b,
                            col(), b, b, b, b, b, b, b]
    

direction = [image_pixels_top,image_pixels_right,image_pixels_bot,image_pixels_left]

while True:
    orientation = random.choice(direction)
    sense.set_pixels(orientation)
    time.sleep(1)
    sense.clear()
    