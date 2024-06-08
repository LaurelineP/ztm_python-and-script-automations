from .read_file import read_file, read_file_with


def get_this_folder_ctx(filename_in_this_folder):
    """[ extra ] Resolve current file path in this current folder """
    import os
    dir_ctx = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(dir_ctx, filename_in_this_folder)
    return path
