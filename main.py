"""
    Main module - gathers all covered code, 
    and also allows to control which section we would like 
    to launch from command line
"""

import sys

import _00_introduction_and_installations as intro
import _01_working_with_files.plain_text as plain_text
import _01_working_with_files.read_file as reader
import _01_working_with_files.write_file as writer
from custom_utils import log_header


# 00 - Working with files
def run_intro():
    """
        Runs the introduction's different computed concepts seen
    """

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
    """
        Runs the working file sections computed concepts seen
    """

    file_path = plain_text.get_this_folder_ctx('text.txt')

    # using "open()" and "file.close"
    reader.read_file(file_path)

    # using "with open()" and "file.close"
    reader.read_file_with(file_path)

    # writing file
    written_file_path = plain_text.get_this_folder_ctx('alpha_test.txt')
    writer.write_line(written_file_path, 'this is a test :) ')
    writer.write_lines(written_file_path, ['one', 'two', 'three'])
    writer.add_to_file(written_file_path, ['four', 'five', 'six'])
    writer.add_to_file(written_file_path, 'end')


# From CLI, Enables to controls what to run
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
