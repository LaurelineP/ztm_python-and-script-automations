"""Playing around with openpyxl / gspread"""

import importlib.util as importlib
import os
from pathlib import Path

import dotenv
import gspread
import openpyxl
from excel_openpyxl import (automate_excel_sheet_create,
                            automate_excel_sheet_import)

# ---------------------------- IMPORT OUTER UTIL ---------------------------- #
custom_utils_path = Path('..', os.getcwd()).resolve() / 'custom_utils.py'
import_spec = importlib.spec_from_file_location(
    'custom_utils', custom_utils_path)
custom_utils = importlib.module_from_spec(import_spec)
import_spec.loader.exec_module(custom_utils)
log_header = custom_utils.log_header


# loading env
ENV = dotenv.load_dotenv('../.env')
print('ENV', ENV)
# print('env_config',env_config)

print('\n\n\n')
log_header('04. Excel Automation', False)
print(' --- excel plain file - openpyxl')
print(' --- google sheet - gspread ')
print('\n\n\n')


def run():
    print('Running Excel Automation')
    # 1.create local excel file
    automate_excel_sheet_create()

    # 2. import content from local excel file
    automate_excel_sheet_import()


run()
