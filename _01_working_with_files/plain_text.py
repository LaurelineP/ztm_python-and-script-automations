"""
	Provide a function to contextualize / refer to the current 
    folder
"""

import os


def get_this_folder_ctx(filename_in_this_folder):
    """[ extra ] Resolve current file path in this current folder """
    dir_ctx = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(dir_ctx, filename_in_this_folder)
    return path
