"""Handling CSV files"""
import csv

from custom_utils import get_curr_dir, log_header

CURRENT_FOLDER = get_curr_dir(__file__)


def read_csv(file_path):
    """Reads CSV file
    Args:
            file_path (str): file absolute path ( csv )
    """
    log_header('read_csv')

    # Get current folder context with the file in the target folder
    file_path = f"{CURRENT_FOLDER}/{file_path}"

    with open(file_path, 'r', encoding="UTF-8") as csv_file:
        content = csv_file.read()
        print('csv_content', content)


def write_csv(file_path, content):
    """Write into CSV
    Args:
            file_path (_type_): _description_
            content (_type_): _description_
    """
    log_header('write_csv')

    # Get current folder context with the file in the target folder
    file_path = f"{CURRENT_FOLDER}/{file_path}"
    print('\t > 1. file:', file_path)

    with open(file_path, 'a', encoding='UTF-8') as csv_file:
        csv_file.write(content)


def read_csv_with_csv(file_path):
    """Reads CSV files using the built-in module cvs
    Args:
            file_path (str): file absolute path ( csv )
    """
    log_header('read_csv_with_csv function')

    # Get current folder context with the file in the target folder
    file_path = f"{CURRENT_FOLDER}/{file_path}"
    print('\t > 1. file:', file_path)

    with open(file_path, 'r', encoding='UTF-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        contents = []
        for row_list in csv_reader:
            contents.append(row_list)
    print(f'\t > 2. file content:\n\t\t "{contents}"')


def write_csv_with_csv(file_path, contents: None, has_headers=False):
    """
    Writes CSV files using the built-in module cvs

    Args:
        file_path (str): file absolute path ( csv )
        contents (list): array structure containing array rows
        has_header (bool): wether in the list there are headers at the 0 index
        Note: DEFAULT_HEADERS = ['name', 'age', 'country', '__default-generated']
    """

    __default_headers = ['name', 'age', 'country', '__default-generated']
    # Ensures to have a list contents
    if contents is None:
        contents = []

    # Writes a csv files
    log_header('write_csv_with_csv function')

    # Get current folder context with the file in the target folder
    file_path = f"{CURRENT_FOLDER}/{file_path}"
    print('\t > 1. file:', file_path)
    with open(file_path, 'w', encoding='UTF-8') as csv_file:
        csv_writer = csv.writer(csv_file)

        if not has_headers and isinstance(contents, list):
            contents.insert(
                0,
                __default_headers
            )

        csv_writer.writerows(contents)
    print(f'\t > 2. file content:\n\t\t "{contents}"')
