from turtle import *
from freegames import line

def grid():
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

def drawx(x, y):
    line(x, y, x + 133, y + 133)
    line(x-0.5, y-0.5, x + 132.5, y + 132.5)
    line(x+0.5, y+0.5, x + 133.5, y + 133.5)
    line(x, y + 133, x + 133, y)
    line(x-0.5, y + 132.5, x + 132.5, y-0.5)
    line(x+0.5, y + 133.5, x + 133.5, y+0.5)


def drawo(x, y):
    up()
    goto(x + 67, y + 5)
    down()
    circle(62)
    up()
    goto(x + 67, y + 5.3)
    down()
    circle(61.7)
    up()
    goto(x + 67, y + 4.7)
    down()
    circle(62.3)


def floor(value):
    return ((value + 200) // 133) * 133 - 200

state = {'player': 0}
players = [drawx, drawo]

def tap(x, y):
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
