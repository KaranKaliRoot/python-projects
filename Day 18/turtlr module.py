import turtle as t
import random
fatass = t.Turtle()
t.colormode(255)
fatass.pensize(2)
fatass.speed("fastest")
def Random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g ,b)
    return random_color
for _ in range(70):
    fatass.circle(100)
    fatass.right(10)
    fatass.color(Random_colors())




Screen = t.Screen()
Screen.exitonclick()