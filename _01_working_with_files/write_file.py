"""
	Provides functions to write into files:
    - write ( by creating or overriding a file ) a line
    - write ( by creating or overriding a file ) multiple lines
    - write ( by adding to a file )
"""

from custom_utils import log_header


def write_line(file_path, content=""):
    """Write a line to a document by creating or overriding it

    Args:
            file_path (str): absolute file path
            content (str, optional): Text to write. Defaults to "".
    """

    log_header('write_line function')
    print('\t > 1. file:', file_path)
    with open(file_path, "w", encoding='UTF-8') as file:
        file.write(content)
    print(f'\t > 2. file content:\n\t\t "{content}"')


def write_lines(file_path, contents=None):
    """Write multiple lines to a document by creating or overriding it

    Args:
                file_path (str): absolute file path
                contents (None, optional): Texts list to write.
    """

    if not isinstance(contents, list):
        contents = [""]

    log_header('write_lines function')
    print('\t > 1. file:', file_path)
    with open(file_path, "w", encoding="UTF-8") as file:
        file.writelines(contents)
    print(f'\t > 2. file content:\n\t\t "{contents}"')


def add_to_file(file_path, any_content):
    """Write by appending content to an existing file

    Args:
            file_path (_type_): _description_
            any_content (_type_): _description_
    """
    log_header('add_to_file function')
    print('\t > 1. file:', file_path)

    with open(file_path, 'a', encoding="UTF-8") as file:
        correct_fn = file.writelines \
            if isinstance(any_content, list) \
            else file.write
        correct_fn(any_content)

    print(f'\t > 2. file content:\n\t\t "{any_content}"')
