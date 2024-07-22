'''Excel using google spread sheet
- requires config keys ( in .env )
'''


import os
from pathlib import Path

import dotenv
import gspread

# ref: = /Users/<user>/Desktop/CODE/ztm/ztm-python-automation
ENV_PATH = Path(__file__).parent.parent / '.env'

# Load's environment configs.
dotenv.load_dotenv(ENV_PATH)
CONFIG = dotenv.dotenv_values(ENV_PATH)
credentials_path = os.path.expanduser(
    CONFIG['GOOGLE_SPREADSHEETS_CREDENTIALS_PATH']
)


DEFAULT_SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# --------------------- CONNECT TO GOOGLE SERVICE ACCOUNT -------------------- #


def connect_to_google_account():
    # gc = None
    print('\n[[ GSpread ] Automate excel sheet - connect to service ]')
    try:
        google_client = gspread.service_account(
            filename=credentials_path,
            scopes=DEFAULT_SCOPES
        )

    # Catches GSpread exceptions
    except gspread.exceptions.GSpreadException as e:
        print(f'\t❌ An error occurred: {e}\n')

    # Catches incorrect path referred to gspread
    except FileNotFoundError as e:
        print(f'\t❌ Credentials file not found: {e}\n')

    # No exceptions > GSpread correctly loaded
    else:
        print("\t> Successfully authenticated with Google Sheets.")

    finally:
        # This block runs whether or not exceptions were raised
        print("\t> Attempt to connect to Google Sheets completed.")

    return google_client


GOOGLE_CLIENT = connect_to_google_account()

# ----------------------------------- UTILS ---------------------------------- #


def get_google_spreadsheet(google_client, filename='python-automation-spreadsheet'):
    '''Gets the google spreadsheet'''
    print('Getting file:', filename)
    try:
        spreadsheet = google_client.open(filename)
        return spreadsheet
    except gspread.exceptions.SpreadsheetNotFound as e:
        print('\t❌ Could not find spreadsheet\n\t\t', e)


# ----------------------------------- LOGIC ---------------------------------- #
# 1. Manipulating an existing sheet
def manipulate_google_sheet(update_content=['A1', 'Hello'], filename='python-automation-spreadsheet'):
    '''Access and manipulate a google spreadsheet'''
    print('\n[[ GSpread ] Automate excel sheet - manipulate: access > edit > save ]')
    spreadsheet = get_google_spreadsheet(GOOGLE_CLIENT, filename)
    print('----', spreadsheet.title)
    # Accessing the worksheet
    worksheet = spreadsheet.sheet1

    # Update logic based on update_content
    UPDATE_CONTENT_LEN = len(update_content)
    if UPDATE_CONTENT_LEN == 2:
        # Adding content to one cell - by cell name and value
        update_and_save = worksheet.update_acell

    elif UPDATE_CONTENT_LEN == 3:
        # Adding content to one cell - by row / column / value position
        update_and_save = worksheet.update_cell

    update_and_save(*update_content)

    # Showing the content in browser
    print('Updated values on sheet', worksheet.get_values())

    # Saving the changes - automatically closes


# 2. Creating a spreadsheet
def create_and_share_google_sheet(filename="python created excel sheet", email=CONFIG['PERSONAL_EMAIL']):
    '''Create a google spreadsheet file'''
    print('\n[[ GSpread ] Automate excel sheet - create ]')

    try:
        spreadsheet = GOOGLE_CLIENT.create(filename)
    except:
        print('❌ [ Creation ] File creation failed')
    finally:
        print('[ Creation ] Completed google sheet creation.')

    # Enables a user to access it ( here it will be us / personal email )
    try:
        spreadsheet.share(
            email,
            'user',
            'writer',
            True
        )
    except:
        print('❌ [ Share ] File sharing failed')
    finally:
        print('[ Share ] Completed google sheet sharing.')
        print('--', len(GOOGLE_CLIENT.openall()))
    return spreadsheet


def clear_created_spreadsheets(filename=None):
    '''Delete one or all service account spreadsheet'''
    spreadsheet_list = GOOGLE_CLIENT.openall()
    print(
        '\t\t> Number List[Spreadsheet]',
        len(spreadsheet_list),
        spreadsheet_list
    )
    if len(spreadsheet_list):
        for spSheet in spreadsheet_list:
            print(f'\tHandling spreadsheet {spSheet}')
            print('--- perm', GOOGLE_CLIENT.list_permissions(spSheet.id)[0])
            del spSheet
            # GOOGLE_CLIENT.del_spreadsheet(spSheet.id)
            # GOOGLE_CLIENT.insert_permission(
            #     file_id=spSheet.id,
            #     value=CONFIG['GOOGLE_ACCOUNT_SERVICE_EMAIL'],
            #     perm_type='user',
            #     role='writer',
            #     notify=True
            # )

    print('Check spreadsheet after clearing', len(GOOGLE_CLIENT.openall()))


def rename_sheet(spreadsheet, name):
    # GOOGLE_CLIENT.
    print('hello - renamesheet')
