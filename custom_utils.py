
"""
    Provides useful development utils 
    - log_header: 3 lines delimiting a header to print for instance
    - log_object: displays an object available properties and methods
"""

import os

#                                    LOGGERS                                   #
# ---------------------------------------------------------------------------- #


def log_header(string, is_upper=True):
    """ Generate header formatted - to identify a section for instance

    Args:
        string (str): header / title in comment
        is_upper (bool, optional): Allows to control wether all the string is 
        transformed or not. Defaults to True.

    Returns:
        str: header - block of lines to depict it as header
    """
    # default constants
    _line_length = 56
    _char = "="
    _char_spaces_num = 2
    _min_char_count = 4

    # string number check - corresponding to length
    string_length = len(string)
    is_customizable = string_length <= (_line_length - _min_char_count * 2)
    if not is_customizable:
        return

    _string = string.upper() if is_upper else string

    # Identify how many characters to fill
    delta = _line_length - string_length
    remainder = delta // 2

    # Prep. tools to construct the string
    char_num = remainder - _char_spaces_num
    char_fill = _char * char_num
    full_line = _char * _line_length

    # Construct lines block
    line_content = f'{char_fill}  {_string}  {char_fill}'
    missing_char_count = _line_length % len(line_content)
    line = _char + line_content \
        if missing_char_count \
        else line_content

    block = f'\n\n{ full_line }\n{ line }\n{ full_line }\n'

    print(block)
    return line


def log_object(obj):
    """Given a python object, this logs its properties and methods"""
    log_header('log object function')

    obj_properties = dir(obj)

    # Filters non-private properties / methods
    details = {'properties': [], 'methods': []}
    for prop in obj_properties:
        is_not_private = not prop.isupper()\
            and not prop.startswith('_')\
            and not prop.endswith('_')
        if is_not_private:
            if callable(getattr(obj, prop)):
                details['methods'].append(prop)
            else:
                details['properties'].append(prop)

    print_msg_properties = f'   > 💡️"{obj.__name__}" {len(details["properties"])} properties: \n\t '
    print_msg_methods = f'   > 💡️"{obj.__name__}" {len(details["methods"])} methods: \n\t '
    print(print_msg_properties, details["properties"])
    print(print_msg_methods, details["methods"])
    return details

# ---------------------------------------------------------------------------- #
#                                  FILE SYSTEM                                 #
# ---------------------------------------------------------------------------- #


def get_this_folder_ctx(filename_in_this_folder, ctx_file=__file__):
    """[ extra ] Resolve current file path in this current folder """
    dir_ctx = os.path.dirname(ctx_file)
    path = os.path.join(dir_ctx, filename_in_this_folder)
    return path


def get_curr_dir(this_file):
    """ Gets current directory / folder name """
    return os.path.dirname(os.path.abspath(this_file))

# read_file.read_file('text.txt')
# """
# Q: How to contextualize this current folder to open the file?
# Instead of taking the context from the command execution
# ( running on the terminal : `python _01_working_with_files/plain_text.py`
# does not find the file as the context is from the project root )
# """
