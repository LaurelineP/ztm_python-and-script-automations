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
from inner_module_utils import jls_extract_def
from project_ex__employees_spreadsheet import (
    add_sheet_content, create_one_employees_spreadsheet)

# ---------------------------- IMPORT OUTER UTIL ---------------------------- #


log_header, log = load_custom_utils()


# loading env
ENV = dotenv.load_dotenv('../.env')

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

    def explore_project_ex__employees_spreadsheet():
        '''explore_project_ex__employees_spreadsheet
            Executes the project example "Employees spreadsheet"
        '''
        log_header('Project Example: Employees Spreadsheet')

        file_path = Path(__file__).parent / 'generated/employees.xlsx'

        # 1. create the spreadsheet files
        create_one_employees_spreadsheet(file_path)

        # 2. Adds a sheet per employee
        contents = [['a1', 'hello'], ['a2', 'world']]
        workbook = add_sheet_content(file_path, 'Kitty', contents)
        print(f'\t> [ EXISTING SHEETS ]\n\t |____{list(workbook.worksheets)}')

    explore_project_ex__employees_spreadsheet()

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
