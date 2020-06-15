import turtle
import time

def erasableWrite(tortoise, name, font, align, reuse=None):
    eraser = turtle.Turtle() if reuse is None else reuse
    eraser.hideturtle()
    eraser.up()
    eraser.setposition(tortoise.position())
    eraser.write(name, font=font, align=align)
    return eraser

t = turtle.Turtle()
t.hideturtle()
t.up()

t.goto(-100,100)
t.write("permanent", font=("Arial", 20, "normal"), align="center")

t.goto(100,100)
eraseble = erasableWrite(t, "erasable", font=("Arial", 20, "normal"), align="center")

time.sleep(1)

eraseble.clear()

t.goto(-100, -100)
erasable = erasableWrite(t, "erasable", font=("Arial", 20, "normal"), align="center", reuse=eraseble)

turtle.done()