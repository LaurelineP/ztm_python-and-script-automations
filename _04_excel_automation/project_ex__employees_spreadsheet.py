
import re
from pathlib import Path

import openpyxl
from inner_module_utils import jls_extract_def

log_header, log = jls_extract_def()

''' Project example Employees Spreadsheet
                                Generate a spreadsheet representing employees
                                with each sheet representing one employees details
'''


def add_sheet_content(filepath, employee_name, contents):
    '''add_sheet_content Add content to a sheet

    Args:
                    filepath (str): filepath name to add sheet to
                    employee_name (str): employee name used as a sheet name
                    contents (list): list of cells position / value
    '''
    log(f'Sheet Creation "{employee_name}"')

    # Sheet loading import file contents
    workbook = openpyxl.load_workbook(filepath)

    # Sheet creation
    worksheets_titles = [ws.title for ws in workbook.worksheets]
    if employee_name not in worksheets_titles:
        workbook.create_sheet(employee_name)
        workbook.save(filepath)

    # Check content and add content to sheet
    has_contents = bool(len(contents))

    cell_pattern = r'^[a-z]\d+$'
    has_valid_contents = all(
        # - should contains a list of 2
        # - and its first item should be of a cell pattern
        len(c) == 2 and re.search(cell_pattern, c[0])
        for c in contents
    )

    # Writes to the employee sheet the provided content
    if has_contents and has_valid_contents:
        for cell, value in contents:
            # Overrides only if value is not the same
            workbook[employee_name][cell] = value

            workbook.save(filepath)
            print(f'\t> Successfully added cell: \n\t |_______ {
                  cell}: {value}\n')

    else:
        print(
            f'Please provide items under the format [ <Cell-Address>, <value> ] {
                contents}'
        )
    return workbook


def create_one_employees_spreadsheet(excel_path: Path, content=[[]]):
    '''create_employees_spreadsheet Create a new employees spreadsheet
            [ from scratch ] - not reusing existing logic personally added ( practice )


    Args:
            excel_path(_type_): excel file path
            content(list, optional): excel sheet content list. Defaults to [].
    '''
    log('EMPLOYEES SPREADSHEET - CREATE')
    # Creates one file employees spreadsheet
    if not Path(excel_path).exists():
        new_spreadsheet = openpyxl.Workbook()
        new_spreadsheet.save(excel_path)
        print(
            f'\t > [ CREATE EMPLOYEE SPREADSHEET ] \n\t "{
                excel_path.name}" file will be created.'
        )
    else:
        print(f'\t > [ CREATE EMPLOYEE SPREADSHEET ] \n\t ▶️ "{
            excel_path.name}" file already exists.'
        )
