import turtle

g = 134
l = 120
input_iteration_to_stop = input("Input the number of line: ")
parse_input_to_int = int(input_iteration_to_stop)
count = 0

while True:
    turtle.left(g)
    turtle.forward(l)
    count += 1
    if parse_input_to_int < count:
        break


turtle.exitonclick()