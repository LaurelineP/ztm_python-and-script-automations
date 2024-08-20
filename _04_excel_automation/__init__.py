"""Playing around with openpyxl / gspread"""

import importlib.util as importlib
import os
from pathlib import Path

import dotenv
from excel_gspread import (connect_to_google_account,
                           create_and_share_google_sheet,
                           create_google_excel_sheet_employees_ranking,
                           create_sheets, delete_created_spreadsheets,
                           delete_sheets, manipulate_google_sheet,
                           rename_sheet)
from excel_openpyxl import CURRENT_DIR as CTX_DIR
from excel_openpyxl import (LOCAL_EXCEL_PATH, LOCAL_SAMPLE_EMPLOYEES_RANTING,
                            automate_excel_spreadsheet_import,
                            create_local_excel_file, create_spreadsheet_sheet,
                            delete_spreadsheet_sheets, do_excel_from_data,
                            get_and_adjust_cells_range, manipulate_cells,
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

    # ---------------------------------------------------------------------------- #
    #                CREATE A LOCAL EXCEL SHEET PROGRAM EXPLORATION                #
    # ---------------------------------------------------------------------------- #
    def explore_openpyxl():
        """Execute functions excel_openpyxl"""

        log('EXCEL AUTOMATION - OPENPYXL')
        # 1.create local excel file
        new_workbook, worksheet, filename = create_local_excel_file()
        print('\t--> filename:', filename)
        print('\t--> worksheet:', worksheet)
        print('\t--> new_workbook:', new_workbook)

        # 2. import content from local excel file
        workbook = automate_excel_spreadsheet_import()

        # 3. create a new spreadsheet sheet
        workbook, sheet, filepath = create_spreadsheet_sheet(
            LOCAL_EXCEL_PATH,
            'new_sheeeeeet'
        )
        print('\t --> sheet', sheet)

        workbook = rename_spreadsheet_sheet(
            LOCAL_EXCEL_PATH,
            'new_sheeeeeet',
            'EXCEL SHEET'
        )

        # deleting a spreadsheet sheet
        sheets_to_remove = []
        for _sh in workbook.worksheets:
            if _sh.title not in ['Sheet', 'EXCEL SHEET']:
                sheets_to_remove.append(_sh.title)
        print('\t--> sheets_to_remove:', sheets_to_remove)

        updated_workbook = delete_spreadsheet_sheets(
            LOCAL_EXCEL_PATH,
            sheets_to_remove
        )
        print('\t--> current workbook up to date:', updated_workbook.worksheets)

        _workbook_content = list(map(
            lambda v: v.title,
            updated_workbook
        ))
        print('\n\n\n--- [ 📌 Workbook Content ]\n------>', _workbook_content)

        # # -------------------------------- CELL FOCUS -------------------------------- #
        manipulate_cells(LOCAL_EXCEL_PATH, 'EXCEL SHEET', [])

        # Ranges [ read, write ]
        ''' Observing the file:
			- as a reader, deduct range for all values in order to have the cell range
			- function will get the range
			- function will adjust:
				- the invalid string cells to empty string
				- the invalid number ( n < 0 -> 0 or n > 10 -> 10)
			- and save this into a new file into the generated folder
        '''
        cells_rows = get_and_adjust_cells_range(
            LOCAL_SAMPLE_EMPLOYEES_RANTING, 'Ratings', 'b3:e11'
        )
        print(f'\n\t> Cells Range: \n\t> {cells_rows}')
        print(f'\t> Cell 1 values: \n\t> {cells_rows[0][0].value}')

        # # data to file
        data_to_excel = [
            ['Products', 'Category', 'Price'],
            ['Iphone', 'Electronic', '1500'],
            ['Eternal Sunshine of the spotless mind', 'culture', '15'],
            ['Sneakers', 'Footwear', '150'],
            ['Dictionary', 'Book', '30'],
        ]
        do_excel_from_data(
            filepath=CTX_DIR / 'generated' / 'data_to_excel.xlsx',
            data=data_to_excel
        )

    explore_openpyxl()
# ---------------------------- PROJECT EXPLORATION --------------------------- #

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

        # ---------------------------------- Project --------------------------------- #
        # Dynamically attribute cells to an employee - creating an employee cells collection
        employees_sheet_values = [
            [('a1', f'Hello {name}!')] for name in employees_names
        ]

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

    # ---------------------------------------------------------------------------- #
    #                    CREATE A GOOGLE EXCEL SHEET EXPLORATION                   #
    # ---------------------------------------------------------------------------- #

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

        # Deleting spreadsheets ( not worksheet )
        delete_created_spreadsheets()

        # Rename sheet
        rename_sheet(
            spreadsheet_title,
            new_spreadsheet.sheet1.title,
            'sheetplop'
        )

        # Create sheets ( worksheet )
        create_sheets(spreadsheet_title, ['one', 'two', 'three'])

        # Delete sheets ( worksheet )
        delete_sheets(spreadsheet_title, ['three'])

    explore_gspread()

    def explore_project_ex__employees_spreadsheet_google():
        create_google_excel_sheet_employees_ranking()
    explore_project_ex__employees_spreadsheet_google()


run()
