import turtle

def draw_square(brad_move):
    for i in range(1,5):
        brad_move.forward(100)
        brad_move.right(90)

def draw_tri(carl_move):
    for i in range(1,4):
        carl_move.forward(100)
        carl_move.right(120)

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("purple")

    #define/create first turtle "brad"
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(3)
    draw_square(brad)

    #define/create second turtle "andy"
    andy = turtle.Turtle()
    andy.shape("turtle")
    andy.color("red")
    andy.speed(5)
    andy.circle(100)

    #define/create thrid turtle "carl"
    carl = turtle.Turtle()
    carl.shape("turtle")
    carl.color("white")
    carl.speed(1)
    draw_tri(carl)

    window.exitonclick()

draw_shapes()
