import turtle
num_circle=20
starting_radius=20
offset=10
animation_speed=5
turtle.speed(animation_speed)
radius=starting_radius
for count in range(num_circle):
    turtle.circle(radius)
    x=turtle.xcor()
    y=turtle.ycor()-offset
    radius+=offset
    turtle.penup
    turtle.goto(x,y)
    turtle.pendown()
turtle.exitonclick()