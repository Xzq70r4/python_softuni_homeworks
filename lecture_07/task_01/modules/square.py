from turtle import Turtle
from lecture_07.task_01.modules.figure import Figure


class Square(Figure):

    def __init__(self, center_x: int=0, center_y: int=0, side: int=0, color: str='black'):
        super().__init__(center_x, center_y, color)
        self.side = side

    def draw(self, turtle: Turtle):
        super().draw(turtle)
        self.jump_to(turtle,
                     self.center_x - self.side/2,
                     self.center_y - self.side/2)

        for _ in range(4):
            turtle.forward(self.side)
            turtle.left(90)

        self.jump_to(turtle, 0, 0)