import turtle

side = input('Input the length of the figure side: ')
angle = input('Input the angle of the figure: ')
parsed_to_int_side = int(side)
parsed_to_int_angle = int(angle)

while True:
    turtle.left(parsed_to_int_angle)
    turtle.forward(parsed_to_int_side)


turtle.exitonclick()