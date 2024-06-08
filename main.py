import os
import sys

from custom_utils import log_header, log_object


# 00 - Introduction & installation code
def run_intro():
    import _00_introduction_and_installations as intro

    # Prompting to let a user interact with the defined logic
    intro.prompt_user()
    print('\n')

    # Text case transformation
    intro.play_with_text('Lowla')
    print('\n')

    # Get time difference
    print(intro.state_date_difference())
    print('\n')


# 01 - Working with files
def run_working_with_files():
    import _01_working_with_files.plain_text as plain_text
    import _01_working_with_files.read_file as reader

    file_path = plain_text.get_this_folder_ctx('text.txt')
    content_1 = reader.read_file(file_path)
    content_2 = reader.read_file_with(file_path)


try:
    programs = {
        "intro": run_intro,
        "files": run_working_with_files
    }
    _this_file, instruction = sys.argv
    programs[instruction]()
except (AttributeError, KeyError):
    log_header("Error")
    print('Invalid program, here are the possible commands:"')
    print('\t>', list(programs.keys()))
