from turtle import Turtle
from lecture_07.task_01.modules.figure import Figure


class Rectangle(Figure):

    def __init__(self, center_x: int=0, center_y: int=0, width: int=0, height: int=0, color: str='black'):
        super().__init__(center_x, center_y, color)
        self.width = width
        self.height = height

    def draw(self, turtle: Turtle):
        super().draw(turtle)
        left = self.center_x - self.width / 2
        down = self.center_y - self.height / 2
        self.jump_to(turtle, left, down)
        for _ in range(2):
            turtle.forward(self.width)
            turtle.left(90)
            turtle.forward(self.height)
            turtle.left(90)

        self.jump_to(turtle, 0, 0)
