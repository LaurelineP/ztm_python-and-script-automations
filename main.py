"""
    Main module - gathers all covered code,
    and also allows to control which section we would like
    to launch from command line
"""


import importlib.util as importlib
import os
import pathlib
import subprocess
import sys

import _00_introduction_and_installations as intro
import _01_working_with_files.csv_data_manipulation as csv_manip
import _01_working_with_files.csv_file as csv_file
import _01_working_with_files.project_product_sales as project1
import _01_working_with_files.read_text as reader
import _01_working_with_files.write_text as writer
import _02_path_and_folders as paths
import _02_path_and_folders.project__files_and_folder_cleaner as project2
import _03_regular_expressions as regexp
import _03_regular_expressions.project__contact_info_extractor as project3
from custom_utils import log_header

CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))
FILE_INPUTS_FOLDER = 'file_inputs'
FILE_OUTPUTS_FOLDER = 'file_outputs'


# import _04_excel_automation as excel


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

    input_filename_in_folder = f'{FILE_INPUTS_FOLDER}/sample-text.txt'

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

    input_filename_in_folder = f'{FILE_INPUTS_FOLDER}/sample-csv.csv'

    # reading a csv file - using csv module
    csv_file.read_csv_with_csv(input_filename_in_folder)

   # --------------------------------- WRITE CSV -------------------------------- #
    output_filename_in_folder = f'{FILE_INPUTS_FOLDER}/sample-csv.csv'

    csv_rows = [
        ['Lowla', 100, 'France'],
    ]

    csv_file.write_csv_with_csv(output_filename_in_folder, contents=csv_rows)

    # ---------------------------- MANIPULATE CSV DATA --------------------------- #
    csv_manip.manipulate_csv(
        f'{FILE_INPUTS_FOLDER}/sample-movies__to-manipulate.csv',
        file_output=f'{
            FILE_OUTPUTS_FOLDER}/sample-movies__to-manipulate__output.csv',
    )


# 02 - Path and folder
def run_paths_and_folders():
    """Runs the paths and folders sections """
    paths.display_paths_details()
    paths.display_paths_details_2()
    paths.iter_over_directory('./_01_working_with_files')
    paths.manage_folder_and_files(
        'create',
        './_02_path_and_folders/work_dir/fake_folder',
    )

    # copy a file
    paths.manage_folder_and_files(
        'copy',
        f'{CURRENT_FOLDER}/README.md',
        # relative to the script parent folder
        './work_dir/README.md'
    )

    # copy a folder ( can be nested )

    # rename
    paths.manage_folder_and_files(
        'rename',
        pathlib.Path('./_02_path_and_folders/work_dir/README.md'),
        './work_dir/README_copy.md'
    )

    paths.manage_folder_and_files(
        'delete',
        pathlib.Path('./_02_path_and_folders/work_dir/folder_to_remove'),
    )

    paths.manage_folder_and_files(
        'delete',
        pathlib.Path('./_02_path_and_folders/work_dir/file_to_remove.txt'),
    )


# 03 - Regular Expressions
def run_regular_expressions():
    """Runs the Regular Expression sections """
    regexp.explore_search()
    regexp.explore_findall()
    regexp.explore_sub()
    regexp.explore_alternation()
    regexp.explore_compilation_flags()


def run_excel():
    """Runs the Spread Sheets automation sections """
    # -------------------------------- SOLUTION 1 --------------------------------
    def run_venv():
        """Runs the venv python and executes the module"""
        venv_python = os.path.join(
            CURRENT_FOLDER, '_04_excel_automation', '_venv_/bin/python3')
        module_path = os.path.join(
            CURRENT_FOLDER, '_04_excel_automation/__init__.py')
        subprocess.run([venv_python, module_path])

    run_venv()

    # -------------------------------- SOLUTION 2: ------------------------------- #
    # https://www.geeksforgeeks.org/python-import-module-outside-directory/

    # print('excel run', excel)
    # print(x)
    # excel.run()


# ---------------------------------------------------------------------------- #
#                                   PROJECTS                                   #
# ---------------------------------------------------------------------------- #


def run_project_product_sales():
    """Project I/O: read and write csv file by adding more columns to be more readable"""
    filename = 'project__product_sales'
    filepath_input = os.path.join(
        CURRENT_FOLDER,
        '_01_working_with_files',
        f'{FILE_INPUTS_FOLDER}/{filename}.txt'
    )
    filepath_output = os.path.join(
        CURRENT_FOLDER,
        '_01_working_with_files',
        f'{FILE_OUTPUTS_FOLDER}/{filename}__output.csv'
    )
    # filepath = pathlib
    project1.run(
        filepath_input,
        filepath_output
    )


def run_project_folder_cleaner():
    """Cleans / Organizes files and folder based on a given file"""
    project2.run()


def run_project_regexp1():
    """Mini project example with regexp -- Mask SSN first sequence"""
    regexp.mask_project()


def run_project_regexp2():
    """Extract contact info"""
    project3.run()


# ---------------------------------------------------------------------------- #
#                                      CLI                                     #
# ---------------------------------------------------------------------------- #
# From CLI, Enables to controls what to run
try:
    programs = {
        "intro": run_intro,
        "files": run_working_with_files,
        "regexp": run_regular_expressions,
        "excel": run_excel,
    }

    projects = {
        "files": run_project_product_sales,
        "paths": run_project_folder_cleaner,
        "regexp": run_project_regexp1,
        "regexp2": run_project_regexp2,
    }

    print(sys.argv)
    if len(sys.argv) < 3:
        raise ValueError('[ Missing command arguments ]')
    _this_file, category, instruction = sys.argv

    if category == 'program':
        programs[instruction]()
    if category == 'project':
        projects[instruction]()

except (AttributeError, KeyError, ValueError) as error:
    log_header("🔥 Error")
    print('Error:', error)
    print('Invalid command, here are the possible commands:"')
    print('\t> python main.py program', list(programs.keys()),
          '\n\t> python main.py project', list(projects.keys()))
