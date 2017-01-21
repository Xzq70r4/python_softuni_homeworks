import lecture_07.task_01.modules.utils as utils


def main():
    figures = utils.create_figures(FIGURES_INPUT_DATA)
    utils.draw_figures(figures)


FIGURES_INPUT_DATA = [
    {"type": "square", "center_x": 0, "center_y": 0, "side": 2, "color": "black"},
    {"type": "square", "center_x": 0, "center_y": 0, "side": 100, "color": "red"},
    {"type": "square", "center_x": 0, "center_y": 0, "side": 200, "color": "blue"},
    {"type": "circle", "center_x": 0, "center_y": 0, "radius": 50, "color": "blue"},
    {"type": "circle", "center_x": 0, "center_y": 0, "radius": 100, "color": "red"},
    {"type": "rectangle", "center_x": 0, "center_y": 0, "width": 100, "height": 200, "color": "orange"},
    {"type": "regular_polygon", "center_x": 0, "center_y": 0, "radius": 250, "num_sides": 9, "color": "purple"},
    {"type": "pie", "center_x": 0, "center_y": 0, "radius": 150, "arg_degrees": 110, "color": "green"},
]

if __name__ == '__main__':
    main()
