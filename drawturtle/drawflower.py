import turtle

def draw_square(move):
    for i in range(1,5):
        move.forward(100)
        move.right(90)

def draw_circle():
    window = turtle.Screen()
    window.bgcolor("black")

    andy = turtle.Turtle()
    andy.shape("arrow")
    andy.color("white")
    andy.speed(100)

    for i in range(1,37):
        draw_square(andy)
        andy.right(10)

def draw_line(bart):
    bart = turtle.Turtle()
    bart.shape("turtle")
    bart.color("green")
    bart.speed(5)
    bart.right(90)
    bart.forward(200)

    window.exitonclick()

draw_circle()
