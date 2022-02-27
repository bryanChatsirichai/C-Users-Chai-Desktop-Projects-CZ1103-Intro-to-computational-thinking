from sense_hat import SenseHat

sense = SenseHat()
import time


w = (255, 255, 255)
bk = (0, 0, 0)
r = (255, 0, 0)
g = (0, 255, 0)
p = (255 ,0, 255)

# This function checks the pitch value and the x coordinate
# to determine whether to move the marble in the x-direction.
# Similarly, it checks the roll value and y coordinate to
# determine whether to move the marble in the y-direction.
#  check x and y
def move_marble(pitch, roll, x, y):
    new_x = x  # assume no change to start with
    new_y = y  # assume no change to start with
    if 1 < pitch < 179 and x != 0:
        new_x -= 1  # move left
    elif 359 > pitch > 179 and x != 7:
        new_x += 1  # move right

    if 1 < roll < 179 and y != 7:
        new_y += 1  # move up
    elif 359 > roll > 179 and y != 0:
        new_y -= 1  # move down

    new_x, new_y = check_wall(x, y, new_x, new_y)
    return new_x, new_y


def check_wall(x, y, new_x, new_y):
    if board[new_y][new_x] != r:
        return new_x, new_y
    elif board[new_y][x] != r:
        return x, new_y
    elif board[y][new_x] != r:
        return new_x, y
    else:
        return x, y



board = [
         [r, r, r, bk, bk, bk, bk, r],
         [r, bk, bk, bk, bk, bk, bk, r],
         [bk, bk, bk, bk, g, r, bk, r],
         [bk, r, r, bk, r, r, bk, r],
         [bk, bk, bk, bk, bk, bk, bk, bk],
         [bk, r, bk, r, r, bk, bk, bk],
         [bk, bk, bk, r, bk, bk, bk, r],
         [r, r, bk, bk, bk, r, r, r]
         ]  # 2d list
y = 0  # y coordinate of marble
x = 0  # x coordinate of marble
board[y][x] = w  # a white marble

gameover = False
while not gameover:
    pitch = sense.get_orientation()['pitch']
    roll = sense.get_orientation()['roll']
    board[y][x] = bk
    x, y = move_marble(pitch, roll, x, y)
    board[y][x] = w
    sense.set_pixels(sum(board, []))  #  convert to 1-dimension list
    time.sleep(0.05)
    if board[2][4] == w:
        gameover = True
sense.show_message('Yay!!')
