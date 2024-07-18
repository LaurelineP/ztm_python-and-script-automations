"""Work with excel sheets
- using openpyxl: module utils for excel sheets


Note for openpyxl vocabulary:
- workbook represents the file excel sheet ( containing inner sheets )
- > worksheet is the sheet within the excel file sheet
"""

from pathlib import Path

import openpyxl

CURRENT_DIR = Path(__file__).parent
LOCAL_EXCEL_NAME = 'local_excel_sheet.xlsx'
LOCAL_EXCEL_PATH = CURRENT_DIR / LOCAL_EXCEL_NAME


# Create & save excel
def automate_excel_sheet_create(filename=LOCAL_EXCEL_PATH):
    '''Create an in memory excel content  - called workbook
              Then saves it
    '''
    if not LOCAL_EXCEL_PATH.exists():
        new_workbook = openpyxl.Workbook()
        new_workbook.save(filename)


# Read excel content
def automate_excel_sheet_import(filename=LOCAL_EXCEL_PATH):
    """Import content of the excel sheet"""
    # workbook: represents excel sheet with openpyxl
    workbook = openpyxl.load_workbook(filename)

    # active first excel file sheet - where we add content
    worksheet = workbook.active

    # cell targeting
    cell_a1 = worksheet['A1']

    # Modifying the cell
    worksheet['A1'] = 'Hello Excel'

    workbook.save(filename)

    print('\t[ ℹ️ workbook ]\t\t', workbook)
    print('\t[ ℹ️ worksheet ]\t\t', worksheet)
    print('\t[ ℹ️ cell_a1 ]\t\t', cell_a1)
    print('\t[ ℹ️ cell_a1 content ]\t', worksheet['A1'])
