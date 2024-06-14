"""
    Main module - gathers all covered code, 
    and also allows to control which section we would like 
    to launch from command line
"""

import os
import sys

import _00_introduction_and_installations as intro
import _01_working_with_files.csv_data_manipulation as csv_manip
import _01_working_with_files.csv_file as csv_file
import _01_working_with_files.read_text as reader
import _01_working_with_files.write_text as writer
from custom_utils import log_header

CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))
FILE_INPUTS_FOLDER = 'file_inputs'
FILE_OUTPUTS_FOLDER = 'file_outputs'

# 00 - Working with files


def run_intro():
    """Runs the introduction's different computed concepts seen"""

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
    """Runs the working file sections computed concepts seen"""
    # ---------------------------------------------------------------------------- #
    #                                  PLAIN TEXT                                  #
    # ---------------------------------------------------------------------------- #
    # --------------------------------- READ TEXT -------------------------------- #

    input_filename_in_folder = f'{FILE_INPUTS_FOLDER}/text.txt'

    # using "open()" and "<file>.close()"
    reader.read_file(input_filename_in_folder)

    # using "with open()" and "<file>.close()"
    reader.read_file_with(input_filename_in_folder)

    # writing text in file - writing a line ( overrides all content )
    output_filename_in_folder = f'{FILE_OUTPUTS_FOLDER}/writing_test.txt'

    # -------------------------------- WRITE TEXT -------------------------------- #
    writer.write_line(output_filename_in_folder, 'this is a test :) ')

    # writing text in file - writing multiple lines ( overrides all content )
    writer.write_lines(output_filename_in_folder, ['one', 'two', 'three'])

    # adding text in file - writing multiple lines ( appending new content / no overrides )
    writer.add_to_file(output_filename_in_folder, ['four', 'five', 'six'])
    writer.add_to_file(output_filename_in_folder, 'end')

    # ---------------------------------------------------------------------------- #
    #                                  CSV RELATED                                 #
    # ---------------------------------------------------------------------------- #
    # --------------------------------- READ CSV --------------------------------- #

    input_filename_in_folder = f'{FILE_INPUTS_FOLDER}/csv.csv'

    # reading a csv file - using csv module
    csv_file.read_csv_with_csv(input_filename_in_folder)

   # --------------------------------- WRITE CSV -------------------------------- #
    output_filename_in_folder = f'{FILE_INPUTS_FOLDER}/csv.csv'

    csv_rows = [
        ['Lowla', 100, 'France'],
    ]

    csv_file.write_csv_with_csv(output_filename_in_folder, contents=csv_rows)

    # ---------------------------- MANIPULATE CSV DATA --------------------------- #
    csv_manip.manipulate_csv(
        f'{FILE_INPUTS_FOLDER}/csv-manipulation_movies.csv',
        file_output=f'{FILE_OUTPUTS_FOLDER}/csv-manipulation_movies__output.csv',
    )


# ---------------------------------------------------------------------------- #
#                                      CLI                                     #
# ---------------------------------------------------------------------------- #
# From CLI, Enables to controls what to run
try:
    programs = {
        "intro": run_intro,
        "files": run_working_with_files
    }
    _this_file, instruction = sys.argv
    programs[instruction]()
except (AttributeError, KeyError) as error:
    log_header("Error")
    print(error)
    print('Invalid program, here are the possible commands:"')
    print('\t>', list(programs.keys()))
