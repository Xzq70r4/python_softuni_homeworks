import sys
import os

FILE_PATH_PATHS_MESSAGE = "File path/paths:"

FILE_NOT_FOUND_MESSAGE = "File not found!!"

FOLDER_NOT_FOUND_MESSAGE = 'Folder not found !!!'

INCORRECT_INPUT_MESSAGE = """
Incorrect input !!!

Example: python3  <script>  <folder>  <file>

- script is name of script in curent case is task_01.py
- folder is name of folder to search file(your choise)
- file is file name you are searching for
 """


def find_file_path(search_folder: str, file_to_find: str) -> list:
    """

    :param search_folder: Is directory where search file
    :param file_to_find: File you are looking for.
    :return Return collection of path/paths or empty list if not found.
    """

    collection_of_file_paths = []

    if file_to_find[-1] == '*':
        file_to_find = file_to_find[:-1]

    for folder_path, _, filenames in os.walk(search_folder):
        for file in filenames:
            if file_to_find == file[:len(file_to_find)]:  # In case file.*
                collection_of_file_paths.append(os.path.join(folder_path, file))

    return collection_of_file_paths


def validate_system_arguments(system_arguments: list) -> bool:
    """

    :param system_arguments: List of inputted arguments.
    :return Bool is parameters are correct or not.
    """

    if len(system_arguments) < 3:
        print(INCORRECT_INPUT_MESSAGE)
        return False
    elif not os.path.exists(system_arguments[1]):
        print(FOLDER_NOT_FOUND_MESSAGE)
        return False
    else:
        return True


if validate_system_arguments(sys.argv):
    folder = sys.argv[1]
    file = sys.argv[2]
    absolute_file_paths = find_file_path(search_folder=folder, file_to_find=file)

    if not absolute_file_paths:
        print(FILE_NOT_FOUND_MESSAGE)
    elif absolute_file_paths:
        print(FILE_PATH_PATHS_MESSAGE)
        for path in absolute_file_paths:
            print(path)
