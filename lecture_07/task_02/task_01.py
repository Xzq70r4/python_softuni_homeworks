import lecture_07.task_02.modules.utils as utils


def main():
    load_input = utils.load_input_data(input_filename=YAML_FILE_PATH)
    figures = utils.create_figures(load_input)
    utils.draw_figures(figures)


JSON_FILE_PATH = './assets/json_shapes.json'
YAML_FILE_PATH = './assets/yaml_shape.yaml'

if __name__ == '__main__':
    main()
