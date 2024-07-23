"""Work with excel sheets
- using openpyxl: module utils for excel sheets


Note for openpyxl vocabulary:
- workbook represents the file excel sheet ( containing inner sheets )
- > worksheet is the sheet within the excel file sheet
"""
from pathlib import Path

import openpyxl

# from custom_utils import log, log_header

CURRENT_DIR = Path(__file__).parent
LOCAL_EXCEL_NAME = 'local_excel_sheet.xlsx'
LOCAL_EXCEL_PATH = CURRENT_DIR / LOCAL_EXCEL_NAME


def automate_excel_sheet_create(filename=LOCAL_EXCEL_PATH):
    '''Create an in memory excel content  - called workbook
                                                                                                                                      Then saves it
    '''
    print('\n[[ OpenPyXl ] Automate excel spreadsheet - Create Spreadsheet ]')
    if not LOCAL_EXCEL_PATH.exists():
        new_workbook = openpyxl.Workbook()
        new_workbook.save(filename)


# Read excel content
def automate_excel_spreadsheet_import(filename=LOCAL_EXCEL_PATH):
    """Import content of the excel sheet"""
    print('\n[[ OpenPyXl ] Automate excel spreadsheet - Edit Spreadsheet Sheet Cell ]')

    # workbook: represents excel sheet with openpyxl
    workbook = openpyxl.load_workbook(filename)

    # active first excel file sheet - where we add content
    current_worksheet = workbook.active

    # cell targeting
    cell_a1 = current_worksheet['A1']

    # Modifying the cell
    current_worksheet['A1'] = 'Hello Excel'

    workbook.save(filename)

    print('\t> [ ℹ️  workbook ]\t\t\t', workbook)
    print('\t> [ ℹ️  current worksheet ]\t\t', current_worksheet)
    print('\t> [ ℹ️  current_worksheet cell_a1 ]\t', cell_a1)
    print('\t> [ ℹ️  current_worksheet content ]\t',
          list(current_worksheet.values), '\n'
          )
    return workbook


def create_spreadsheet_sheet(workbook_path, new_sheet_name):
    '''create_spreadsheet_sheet Creates a spreadsheet's sheet

    Args:
        workbook_path (str): path of the local file
        new_sheet_name (str): name of the sheet to create

    Returns:
        Worksheet: The spreadsheet's worksheet
    '''
    print('\n[[ OpenPyXl ] Automate excel spreadsheet - Create Spreadsheet Sheet ]')

    # Loads the spreadsheet file as a workbook
    workbook = openpyxl.load_workbook(workbook_path)

    # Create a spreadsheet's sheet ( after the first sheet )
    if any(ws.title != new_sheet_name for ws in workbook.worksheets):
        print(f'\t> [ Sheet Creation ] Creating new sheet "{new_sheet_name}"')
        workbook.create_sheet(new_sheet_name, 1)
    else:
        print(
            f'\t > [ Sheet creation ] Sheet "{
                new_sheet_name}" already exist'
        )

    # Save modification
    workbook.save(workbook_path)

    # Returns a sheet
    return workbook[new_sheet_name]


def rename_spreadsheet_sheet(filepath, sheet_name, new_sheet_name):
    '''rename_spreadsheet_sheet Renames Spreadsheet sheet

    Args:
        filepath (str): path of the excel spreadsheet file
        sheet_name (str): name of the spreadsheet sheet
        new_sheet_name (str): new name for the spreadsheet sheet

    Returns:
        Workbook: the modified workbook
    '''
    print('\n[[ OpenPyXl ] Automate excel spreadsheet - Rename Spreadsheet sheet ]')
    workbook = openpyxl.load_workbook(filepath)
    try:
        if not workbook[sheet_name]:
            print(
                f'\t> [ Sheet Rename ] ❌ Inexistent sheet "{sheet_name}"'
            )
        else:
            workbook[sheet_name].title = new_sheet_name
            _workbook_content = list(map(
                lambda v: v.title,
                workbook.worksheets
            ))
            workbook.save(filepath)
            print(
                '\t> [ Sheet Rename ] Sheet {sheet_name} renamed as {new_sheet_name}'
            )
            return workbook
    except:
        print(
            f'\t> [ Sheet Rename ] ❌ Error on rename inexistent sheet "{
                sheet_name}" as "{new_sheet_name}"'
        )


def delete_spreadsheet_sheets(filepath, sheet_names):
    '''delete_spreadsheet_sheets Deletes multiple sheets from a Spreadsheet

    Args:
            filepath (str): path of the excel file
            sheet_names (list): list of the spreadsheet sheet names

    Returns:
            Workbook: Modified Workbook
    '''
    print('\n[[ OpenPyXl ] Automate excel spreadsheet - Delete Spreadsheet sheets ]')
    workbook = openpyxl.load_workbook(filepath)
    for sheet_name in sheet_names:
        try:
            print(f'\t> [ Sheet Deletion ] Deleting "{sheet_name}"')
            del workbook[sheet_name]

        except:
            print('\t\t> Could not delete sheet "{sheet_name}"')

    workbook.save(filepath)
    return workbook
