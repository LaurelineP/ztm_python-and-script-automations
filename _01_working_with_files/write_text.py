"""
	Provides functions to write into files:
    - write ( by creating or overriding a file ) a line
    - write ( by creating or overriding a file ) multiple lines
    - write ( by adding to a file )
"""
import os

from custom_utils import get_curr_dir, get_this_folder_ctx, log_header

CURRENT_FOLDER = get_curr_dir(__file__)
CURRENT_FOLDER_FILE = f'{CURRENT_FOLDER}/file_outputs'
OUTPUT_FILES_FOLDER_ABS = get_this_folder_ctx(CURRENT_FOLDER_FILE, __file__)


def ensure_access_output_folder():
    """Ensures the output folder does exist"""
    if not os.path.exists(OUTPUT_FILES_FOLDER_ABS):
        os.makedirs(OUTPUT_FILES_FOLDER_ABS)
    else:
        return


ensure_access_output_folder()


def write_line(file_path, content=""):
    """Write a line to a document by creating or overriding it

    Args:
            file_path (str): absolute file path
            content (str, optional): Text to write. Defaults to "".
    """

    log_header('write_line function')

    # Get current folder context with the file in the target folder
    file_path = f"{CURRENT_FOLDER}/{file_path}"

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

    # Get current folder context with the file in the target folder
    file_path = f"{CURRENT_FOLDER}/{file_path}"
    print('\t > 1. file:', file_path)

    with open(file_path, "w", encoding="UTF-8", newline="\n") as file:
        file.writelines(f'{item}\n' for item in contents)
    print(f'\t > 2. file content:\n\t\t "{contents}"')


def add_to_file(file_path, any_content):
    """Write by appending content to an existing file

    Args:
            file_path (_type_): _description_
            any_content (_type_): _description_
    """
    log_header('add_to_file function')

    # Get current folder context with the file in the target folder
    file_path = f"{CURRENT_FOLDER}/{file_path}"
    print('\t > 1. file:', file_path)

    with open(file_path, 'a', encoding="UTF-8") as file:
        correct_fn = file.writelines \
            if isinstance(any_content, list) \
            else file.write
        correct_fn(any_content)

    print(f'\t > 2. file content:\n\t\t "{any_content}"')
