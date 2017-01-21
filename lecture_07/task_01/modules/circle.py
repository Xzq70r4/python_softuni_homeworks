from turtle import Turtle
from lecture_07.task_01.modules.figure import Figure


class Circle(Figure):
    steps = None

    def __init__(self, center_x: int=0, center_y: int=0, radius: int=0, color: str='black'):
        super().__init__(center_x, center_y, color)
        self.radius = radius

    def draw(self, turtle: Turtle):
        super().draw(turtle)
        self.jump_to(turtle, self.center_x, self.center_y - self.radius)
        turtle.circle(self.radius, steps=self.steps)
        self.jump_to(turtle, 0, 0)