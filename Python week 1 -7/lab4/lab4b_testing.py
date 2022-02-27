from sense_hat import SenseHat
sense = SenseHat()
import time
import random
r = (255,0,0)
g = (0,255,0)
b= (0,0,255)
y = (255,255,0)
p = (255,0,255)
colour = [r,g,b,y]
choose = random.choice(colour)
print(choose)
sense.clear()


while True:
    image_pixels_top =    [r, r, r, r, r, r, r, r,
                            b, b, b, b, b, b, b, b,
                            b, b, b, b, b, b, b, b,
                            b, b, b, b, b, b, b, b,
                            b, b, b, b, b, b, b, b,
                            b, b, b, b, b, b, b, b,
                            b, b, b, b, b, b, b, b,
                            b, b, b, b, b, b, b, b]
  
    image_pixels_right =    [b, b, b, b, b, b, b, g,
                            b, b, b, b, b, b, b, g,
                            b, b, b, b, b, b, b, g,
                            b, b, b, b, b, b, b, g,
                            b, b, b, b, b, b, b, g,
                            b, b, b, b, b, b, b, g,
                            b, b, b, b, b, b, b, g,
                            b, b, b, b, b, b, b, g]
                            
    image_pixels_bot =    [b, b, b, b, b, b, b, b,
                            b, b, b, b, b, b, b, b,
                            b, b, b, b, b, b, b, b,
                            b, b, b, b, b, b, b, b,
                            b, b, b, b, b, b, b, b,
                            b, b, b, b, b, b, b, b,
                            b, b, b, b, b, b, b, b,
                            y, y, y, y, y, y, y, y]
        
    image_pixels_left =    [p, b, b, b, b, b, b, b,
                            p, b, b, b, b, b, b, b,
                            p, b, b, b, b, b, b, b,
                            p, b, b, b, b, b, b, b,
                            p, b, b, b, b, b, b, b,
                            p, b, b, b, b, b, b, b,
                            p, b, b, b, b, b, b, b,
                            p, b, b, b, b, b, b, b]
    
    

    sense.set_pixels(image_pixels_top)
    time.sleep(1)
    sense.clear()
    sense.set_pixels(image_pixels_right)
    time.sleep(1)
    sense.clear()
    sense.set_pixels(image_pixels_bot)
    time.sleep(1)
    sense.clear()
    sense.set_pixels(image_pixels_left)
    time.sleep(1)
    sense.clear()