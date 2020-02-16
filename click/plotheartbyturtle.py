import turtle
import numpy as np
import time

# install turtle
# download turtle-0.0.2.tar.gz then
# pip install -e ./turtle-0.0.2

me1 = turtle.Turtle()
me1.shape('arrow')
me1.speed(0)
me1.penup()
me1.color('red')

# (|x|-1)^2+y^2 = 1 => y1 = √(1-(|x|-1)^2)
def f1(x):
    return (1 - (abs(x) - 1)**2)**0.5

# y2 = -3√(1-√(|x|/2))
def f2(x):
    return -3*(1 - (abs(x)/2)**0.5)**0.5

colors = ['#F0F', '#90F']
color_idx = 0

for x in np.linspace(-2, 2, 200):
    me1.color(colors[color_idx % 2])
    y1 = f1(x)
    me1.goto(x*100, y1*100)
    me1.pendown()
    color_idx += 1

    me1.color(colors[color_idx % 2])
    y2 = f2(x)
    me1.goto(x*100, y2*100)
    color_idx += 1

me1.hideturtle()
me1.penup()

text = 'HAPPY VALENTINES DAY'
me1.color( 'white')
me1.goto(-80,-80)

for lett in text:
    me1.pendown()
    me1.write(lett,font='200px')
    me1.penup()
    me1.setx(me1.pos()[0] + 8)
    time.sleep(0.05)

time.sleep(5)