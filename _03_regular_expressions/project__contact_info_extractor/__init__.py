"""Extracts info from file ( using regular expression )
- phone numbers
- email addresses
- website addresses
Writing a the result to their own respective text files
"""


import re
import shutil
import sys
from pathlib import Path

from custom_utils import log_header

CURRENT_FOLDER = Path(__file__).parent

storing_folder = CURRENT_FOLDER / 'contact_info'


def set_output_folder(folder_path: Path):
    """Ensure output folder clean and creation for each execution """
    # Clearing each time previous attempts
    if folder_path.exists() and folder_path.is_dir():
        shutil.rmtree(folder_path)

    # Re-build contact-info folder
    if not Path(folder_path).exists():
        Path(folder_path).mkdir()


def includes_items(values, collector: list):
    """Includes values in collector if the item is not within"""
    for value in values:
        if value not in collector:
            collector.append(value)
    return collector


def read_and_extract(path: Path):
    """Read and extract contact info"""
    log_header('RegExp - read_and_extract')
    collection = {
        "phones": [],
        "emails": [],
        "websites": [],
    }

    with open(path, "r", encoding='UTF-8') as file:
        reg_american_phone = r'(\(?\d{3}\)?.?\d{3}.\d{4})'
        reg_email = r'((?:[a-z-A-Z_0-9\.]+@)[a-z-A-Z_0-9]+\.\w{2,3})'
        reg_website = r'((?:https?:\/\/)?(?:www\.)?[a-z-A-Z_0-9]+\.(?:com|net|io|org))'

        for line in file.readlines():
            matched_phones = re.findall(reg_american_phone, line)
            matched_emails = re.findall(reg_email, line)
            matched_websites = re.findall(reg_website, line)

            if len(matched_phones):
                collection["phones"] = includes_items(
                    matched_phones,
                    collection["phones"]
                )

            if len(matched_emails):
                collection["emails"] = includes_items(
                    matched_emails,
                    collection["emails"]
                )

            if len(matched_websites):
                collection["websites"] = includes_items(
                    matched_websites,
                    collection["websites"]
                )

    # Dynamically write file for each collected info
    for key, item in collection.items():
        file_path = storing_folder / f'{key}.txt'
        with open(file_path, 'w', encoding='UTF-8') as file:
            _values = '\n'.join(item)
            file.writelines(_values)


def run(path_string: str = ''):
    """Runs the project: will extract contact info from given file"""
    _path = path_string
    try:
        while not _path:
            _path = input(
                'Please provide the file path to extract contact info from: \n\t> ')
            if not _path:
                print('❌  Please provide a valid path.\n\n')
    except KeyboardInterrupt:
        sys.exit()

    path = Path(_path)
    if path.exists():
        set_output_folder(storing_folder)
        read_and_extract(path)
