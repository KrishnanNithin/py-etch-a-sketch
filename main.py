import turtle

# Initializes objects
t = turtle.Turtle()
screen = turtle.Screen()

#Defines functions
def move_forwards():
    t.forward(10)

def turn_left():
    t.left(10)

def move_backwards():
    t.backward(10)

def turn_right():
    t.right(10)
def clear_screen():
    t.reset()


# Initializes key listeners
screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="c", fun=clear_screen)

screen.exitonclick()