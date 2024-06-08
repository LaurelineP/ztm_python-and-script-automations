from custom_utils import log_header


def read_file(file_path):
    """Opening a file from this current folder context using 'open'"""
    print('ye')

    log_header('READ_FILE FUNCTION')

    # Open and read file
    file = open(file_path, 'r')
    file_content = file.read()
    file.close()

    # Printable message
    print(f'\t > 2. file content:\n\t\t "{file_content}"')
    return file_content


def read_file_with(file_path):
    """Opening file from the current folder using 'with'"""

    log_header('READ_FILE_WITH FUNCTION')

    print('\t > 1. file:', file_path)

    # Open and read file - self-contained - using "with"
    file_content = ''
    with open(file_path, 'r') as file:
        file_content = file.read()

    print(f'\t > 2. file content:\n\t\t "{file_content}"')
    return file_content
