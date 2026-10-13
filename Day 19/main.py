from turtle import Turtle, Screen
fatass = Turtle()
jackass = Turtle()
my_screen = Screen()
fatass.shape("turtle")
jackass.shape("turtle")
fatass.color("green")
jackass.color("red")
jackass.goto(x=-100, y=0)
def move_left():
    fatass.left(10)
    jackass.right(10)
def move_backwards():
    fatass.backward(10)
    jackass.forward(10)
def move_right():
    fatass.right(10)
    jackass.left(10)
def move_forwards():
    fatass.forward(10)
    jackass.backward(10)
my_screen.listen()
my_screen.onkey(key="w", fun=move_forwards)
my_screen.onkey(key="d", fun=move_right)
my_screen.onkey(key="a", fun=move_left)
my_screen.onkey(key="s", fun=move_backwards)
my_screen.exitonclick()

