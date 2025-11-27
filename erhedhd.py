import turtle

def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_chakra(x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.color("navy")
    turtle.circle(radius)

    # Draw 24 spokes
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for i in range(24):
        turtle.forward(radius)
        turtle.backward(radius)
        turtle.right(15)

def draw_indian_flag():
    turtle.speed(10)
    turtle.title("Indian Flag")

    # Flag dimensions
    width = 600
    height = 300
    stripe_height = height / 3

    # Saffron stripe
    draw_rectangle("orange", -width/2, height/2, width, stripe_height)

    # White stripe
    draw_rectangle("white", -width/2, height/2 - stripe_height, width, stripe_height)

    # Green stripe
    draw_rectangle("green", -width/2, height/2 - 2*stripe_height, width, stripe_height)

    # Ashoka Chakra in the center of white stripe
    draw_chakra(0, height/2 - stripe_height - stripe_height/2, 40)

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    draw_indian_flag()

