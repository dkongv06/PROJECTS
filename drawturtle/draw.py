import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("blue")

    #turtle1
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(5)

    #brad moves
    moves = 0
    total_moves = 4
    while(moves < total_moves):
        brad.forward(50)
        brad.right(90)
        moves = moves + 1

    #turtle2
    andy = turtle.Turtle()
    andy.shape("turtle")
    andy.color("red")
    andy.speed(1)

    #andy moves
    andy.circle(100)

    #turtle3
    carl = turtle.Turtle()
    carl.shape("turtle")
    carl.color("orange")
    carl.speed(3)

    #carl moves
    moves = 0
    total_moves = 3
    while(moves < total_moves):
        carl.forward(50)
        carl.right(120)
        moves = moves + 1
    
    window.exitonclick()

draw_shapes()
