import os
from turtle import Turtle, done as turtle_done

from lecture_07.task_02.modules.shapes.circle import Circle
from lecture_07.task_02.modules.shapes.square import Square
from lecture_07.task_02.modules.shapes.rectangle import Rectangle
from lecture_07.task_02.modules.shapes.pie import Pie
from lecture_07.task_02.modules.shapes.regular_polygon import RegularPolygon

from lecture_07.task_02.modules.reader.json_reader import JSONLoader
from lecture_07.task_02.modules.reader.yaml_reader import YAMLLoader


def load_input_data(input_filename):
    filename, extension = os.path.splitext(input_filename)
    loader = None
    if extension == '.json':
        loader = JSONLoader(input_filename)
    elif extension == '.yaml':
        loader = YAMLLoader(input_filename)

    if loader is not None:
        return loader.load()
    else:
        raise ValueError("Unsupported file format: {}".format(extension))


def create_figures(figures_input_data: list) -> list:
    """
    Return a list of Figure instances
    :param figures_input_data: List of dict
    :return: result: list of parsed figure object
    """
    result = []
    for fdata in figures_input_data:
        type = fdata['type']
        if type == 'square':
            figure = Square(
                center_x=fdata['center_x'],
                center_y=fdata['center_y'],
                side=fdata['side'],
                color=fdata['color'],
            )

        elif type == 'circle':
            figure = Circle(
                center_x=fdata['center_x'],
                center_y=fdata['center_y'],
                radius=fdata['radius'],
                color=fdata['color'],
            )

        elif type == 'rectangle':
            figure = Rectangle(
                center_x=fdata['center_x'],
                center_y=fdata['center_y'],
                width=fdata['width'],
                height=fdata['height'],
                color=fdata['color']
            )

        elif type == 'pie':
            figure = Pie(
                center_x=fdata['center_x'],
                center_y=fdata['center_y'],
                radius=fdata['radius'],
                arg_degrees=fdata['arg_degrees'],
                color=fdata['color'],
            )

        elif type == 'regular_polygon':
            figure = RegularPolygon(
                center_x=fdata['center_x'],
                center_y=fdata['center_y'],
                radius=fdata['radius'],
                num_sides=fdata['num_sides'],
                color=fdata['color'],
            )

        else:
            raise Exception("Unsupported figure type: " + type)
        result.append(figure)

    return result


def draw_figures(figures):
    t = Turtle()
    t.speed("fastest")

    for figure in figures:
        figure.draw(t)

    turtle_done()
