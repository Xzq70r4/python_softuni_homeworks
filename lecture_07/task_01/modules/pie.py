from turtle import Turtle
from lecture_07.task_01.modules.figure import Figure


class Pie(Figure):
    steps = None

    def __init__(self, center_x: int=0, center_y: int=0, radius: int=0, arg_degrees: int=0, color: str='black'):
        super().__init__(center_x, center_y, color)
        self.radius = radius
        self.arg_degrees = arg_degrees

    def draw(self, turtle: Turtle):
        super().draw(turtle)
        self.jump_to(turtle, self.center_x, self.center_y)
        turtle.begin_fill()
        turtle.forward(self.radius)
        turtle.left(90)
        turtle.circle(self.radius, extent=self.arg_degrees)
        turtle.left(90)
        turtle.forward(self.radius)
        turtle.end_fill()
        self.jump_to(turtle, 0, 0)
