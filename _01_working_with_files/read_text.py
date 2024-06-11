"""
	Reads file - 2 ways, with: 
	- a simple `open()`
	- a `with open()`
"""


from custom_utils import get_curr_dir, log_header

CURRENT_FOLDER = get_curr_dir(__file__)


def read_file(file_path):
    """Opening a file from this current folder context using 'open'"""
    log_header('READ_FILE FUNCTION')

    # Get current folder context with the file in the target folder
    file_path = f"{CURRENT_FOLDER}/{file_path}"

    # Open and read file
    file = open(file_path, 'r', encoding="utf-8")
    file_content = file.read()
    file.close()

    # Printable message
    print(f'\t > 2. file content:\n\t\t "{file_content}"')
    return file_content


def read_file_with(file_path):
    """Opening file from the current folder using 'with'"""

    log_header('READ_FILE_WITH FUNCTION')

    # Get current folder context with the file in the target folder
    file_path = f"{CURRENT_FOLDER}/{file_path}"

    print('\t > 1. file:', file_path)

    # Open and read file - self-contained - using "with"
    file_content = ''
    with open(file_path, 'r', encoding="utf-8") as file:
        file_content = file.read()

    print(f'\t > 2. file content:\n\t\t "{file_content}"')
    return file_content
