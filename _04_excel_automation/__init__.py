"""Playing around with openpyxl / gspread"""

import importlib.util as importlib
import os
from pathlib import Path

import dotenv
from excel_gspread import (clear_created_spreadsheets,
                           connect_to_google_account,
                           create_and_share_google_sheet,
                           manipulate_google_sheet, rename_sheet)
from excel_openpyxl import (LOCAL_EXCEL_PATH, automate_excel_sheet_create,
                            automate_excel_spreadsheet_import,
                            create_spreadsheet_sheet,
                            delete_spreadsheet_sheets,
                            rename_spreadsheet_sheet)
from inner_module_utils import (load_custom_utils, load_module,
                                load_module_from_path)
from project_ex__employees_spreadsheet import generate_employees

# ---------------------------- IMPORT OUTER UTIL ---------------------------- #


log_header, log, log_object = load_custom_utils()

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

        # ----------------------------------- PATHS ---------------------------------- #
        file_path = Path(__file__).parent / 'generated/employees.xlsx'
        if not file_path.parent.exists():
            os.makedirs(file_path.parent)

        # -------------------------------- MOCKED DATA ------------------------------- #
        employees_names = ['Jane Doe', 'John Smith']

        # Describes employee overview on first 'Sheet' at the first column
        root_sheet_values = [
            (f'a{idx+1}', name) for idx, name in enumerate(employees_names)
        ]

        # Dynamically attribute cells to an employee - creating an employee cells collection
        employees_sheet_values = [
            [('a1', f'Hello {name}!')] for name in employees_names
        ]

        # ---------------------------------- Project --------------------------------- #
        generate_employees(
            file_path,
            # Sheet to create
            ['Sheet', *employees_names],

            # Sheets' content referring to employee name index
            [
                root_sheet_values,
                *employees_sheet_values
            ]
        )

    explore_project_ex__employees_spreadsheet()

    def explore_gspread():
        """Execute functions excel_gspread"""

        log('EXCEL AUTOMATION - GSPREAD')

        # google client
        gc = connect_to_google_account()

        # Updates by targeting a cell and providing the value
        manipulate_google_sheet(update_content=['A1', 'Aloha'])

        # Updates by coordinations values
        manipulate_google_sheet(update_content=[3, 3, 'Hello Bis'])

        new_spreadsheet = create_and_share_google_sheet('23/07/2024')
        spreadsheet_title = new_spreadsheet.title
        print(f'Created spread sheet title: {spreadsheet_title}')

        # Modifies a specifics spreadsheet
        manipulate_google_sheet(
            filename=spreadsheet_title,
            update_content=['A1', 'New Spreadsheet']
        )

        # Deleting spreadsheets
        # clear_created_spreadsheets()

        rename_sheet(spreadsheet_title, 'New Spreadsheet', 'sheetplop')
    # explore_gspread()


run()
