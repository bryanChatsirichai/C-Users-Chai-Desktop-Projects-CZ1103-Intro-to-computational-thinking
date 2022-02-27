def conversion_colour(x):
    while True:
        try:
            x = int(x)
        except:
            print("Not a number")
            x = input("Enter a number")
            continue
        if 0 <= x <= 255:
            return x
        else:
            print("Out of range")
            x = input('Enter between 0 to 255')
            continue

def conversion_speed(spd):
    while True:
        try:
            spd = float(spd)
            return spd
        except:
            print("Not a number")
            spd = input("Enter a number")
            continue

def spd():
    speed = input('Enter the speed of text')
    speed = conversion_speed(speed)
    return speed

def rgbtext():
    red = input("Enter the value of the red colour for message")
    r = conversion_colour(red)
    green = input("Enter the value of the green colour for message")
    g = conversion_colour(green)
    blue = input("Enter the value of the blue colour for message")
    b = conversion_colour(blue)
    return r, g, b

def rgbback():
    redbg = input("Enter the value of the red colour for background")
    rback = conversion_colour(redbg)
    greenbg = input("Enter the value of the green colour for background")
    gback = conversion_colour(greenbg)
    bluebg = input("Enter the value of the blue colour for background")
    back = conversion_colour(bluebg)
    return rback, gback, back

def display(word):
    speed_text = spd()
    text_colour = rgbtext()
    background_colour = rgbback()
    count = 1
    while count < 3:
        if text_colour == background_colour:
            count += 1
            print('same colour setting please re enter')
            print('this is try number {}'.format(count))
            text_colour = rgbtext()
            background_colour = rgbback()
        elif text_colour != background_colour:
            break
    else:
        print('Exit as fail 3 times')
    print(word,speed_text, text_colour, background_colour) #treat as sense_hat printing


display(input('Enter display text'))