"""Playing around with openpyxl / gspread"""

import importlib.util as importlib
import os
from pathlib import Path

import dotenv
from excel_gspread import (clear_created_spreadsheets,
                           connect_to_google_account,
                           create_and_share_google_sheet,
                           manipulate_google_sheet)
from excel_openpyxl import (LOCAL_EXCEL_PATH, automate_excel_sheet_create,
                            automate_excel_spreadsheet_import,
                            create_spreadsheet_sheet,
                            delete_spreadsheet_sheets,
                            rename_spreadsheet_sheet)

# ---------------------------- IMPORT OUTER UTIL ---------------------------- #
custom_utils_path = Path('..', os.getcwd()).resolve() / 'custom_utils.py'
import_spec = importlib.spec_from_file_location(
    'custom_utils', custom_utils_path)
custom_utils = importlib.module_from_spec(import_spec)
import_spec.loader.exec_module(custom_utils)
log_header = custom_utils.log_header
log = custom_utils.log


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

    def explore_openpyxl():
        """Execute functions excel_openpyxl"""

        log('EXCEL AUTOMATION - OPENPYXL')
        # 1.create local excel file
        new_worksheet = automate_excel_sheet_create()

        # 2. import content from local excel file
        workbook = automate_excel_spreadsheet_import()
        worksheets = workbook.worksheets

        # 3. create a new spreadsheet sheet
        sheet = create_spreadsheet_sheet(
            LOCAL_EXCEL_PATH, 'new_sheeeeeet'
        )
        # print('---sheet', sheet)

        rename_spreadsheet_sheet(
            LOCAL_EXCEL_PATH,
            'new_sheeeeeet4',
            'EXCEL SHEET'
        )

        # deleting a spreadsheet sheet
        sheets_to_remove = []
        for _sh in worksheets:
            if _sh.title not in ['Sheet', 'EXCEL SHEET']:
                sheets_to_remove.append(_sh.title)

        updated_workbook = delete_spreadsheet_sheets(
            LOCAL_EXCEL_PATH,
            sheets_to_remove
        )

        _workbook_content = list(map(
            lambda v: v.title,
            updated_workbook
        ))
        print('\n\n\n--- [ 📌 Workbook Content ]\n------>', _workbook_content)

    explore_openpyxl()

    def explore_gspread():
        """Execute functions excel_gspread"""

        log('EXCEL AUTOMATION - GSPREAD')

        connect_to_google_account()

        # Updates by targeting a cell and providing the value
        # manipulate_google_sheet(update_content=['A1', 'Hello'])

        # Updates by coordinations values
        # manipulate_google_sheet(update_content=[3, 3, 'Hello Bis'])

        # new_spreadsheet = create_and_share_google_sheet()
        # spreadsheet_title = new_spreadsheet.title
        # print(f'Created spread sheet title: {spreadsheet_title}')

        # Modifies a specifics spreadsheet
        # manipulate_google_sheet(
        #     filename=spreadsheet_title,
        #     update_content=['A1', 'New Spreadsheet']
        # )

        # Deleting spreadsheets
        # clear_created_spreadsheets()

    explore_gspread()


run()
