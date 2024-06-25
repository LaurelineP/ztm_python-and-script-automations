"""Clean any given folder path
- 0 - request correct path
- 1 - check for correct input path
- 2 - create folders to organize the files within
- 3 - clean folder
    - deducting logic to handle different files
    - removes or moves files/folders to their corresponding folders
"""

import re as reg
from pathlib import Path
from shutil import move, rmtree

from custom_utils import log_header

HOME = Path().home()
DESKTOP = HOME / 'Desktop'
ORGANIZED_FOLDER = 'organized'




def request_path():
    """Request path of a folder to clean"""
    log_header('request_path')
    instructions = "Please provide a folder path ( copy/paste it ):\n\t> "
    path = input(instructions)
    return path

def check_is_correct_input(path: Path):
    """Checks if user input is correct"""
    does_exist = path.exists()
    if does_exist:
        return False\
            if (path.is_file() or not does_exist)\
            else True

def create_folders(organized_folder_path: Path, sub_folders: list):
    """Creates folders to organize files and folder within given path"""
    if not organized_folder_path.exists():
        print('\t> Organize_folder_path', organized_folder_path)
        organized_folder_path.mkdir()

    # Creates sub-folders ( text_files, csv_files, folders )
    for sub_folder in sub_folders:
        sub_folder_target = sub_folder if isinstance(sub_folder, str) else sub_folder[0]
        sub_folder_path = organized_folder_path / sub_folder_target
        if not sub_folder_path.exists():
            sub_folder_path.mkdir()

def organize_each_folder_item(original_path: Path, organized_folder_path: Path, sub_folders: list):
    """Organize each folder item ( files or folder and temp content )"""
    folder_iter = original_path.iterdir()
    print(f'\n\t> 📌 Handling:')
    for content_path in folder_iter:
        kind = 'File' if content_path.is_file() else 'Folder'
        kind_icon = '📃' if content_path.is_file() else '🗂️ '
        if(content_path.name != "organized" ):
            print(f'\t|____ ✨ { kind_icon } { kind } { content_path.name }...')
	
            # Removes temporary files and folders
            is_temp = len(reg.findall(
                'temp|temporary',
                str(content_path)
            )) > 0
            if is_temp:
                rmtree(content_path)
                print(f'\t     |___ deleted temporary {kind}\n\n')


            # Organize folders
            elif content_path.is_dir():
                move(content_path, organized_folder_path/'folders/')
                print(f'\t     |___ moved to folders/\n\n')


            # Organize files
            else:
                # Dynamically move the file to its corresponding folder
                # Find index of item containing ( next -> access first, n for n in list --> iterates, if --> filters )
                folder_target = next(
                    # find folder target ( (n for n in list if <condition>) )
                    (
                        item[0] for item in sub_folders
                            if isinstance(item, tuple)
                            and item[1] in str(content_path)
                    ),
                    # default folder target ( last of sub_folders )
                   None
                )
                
                target_folder_path  = organized_folder_path if not folder_target else organized_folder_path/folder_target
                move(content_path , target_folder_path)
                print(f'\t     |___ to', 'root' if not folder_target else folder_target + '/', 'folder\n\n')

def clean_folder(original_path: Path):
    """Organize the requested folder"""

    # Creates the "organized" folder and its sub_folders
    organized_folder_path = Path(original_path,ORGANIZED_FOLDER)
    # TODO: must be scalable - sub folders should be passed as args too 
    # Describes which folder for which kind of file
    sub_folders = [('text_files', '.txt'),('csv_files', '.csv'), 'folders']
    create_folders(organized_folder_path, sub_folders)

    # Iterates over original folder files
    organize_each_folder_item(
        original_path,
        organized_folder_path,
        sub_folders
    )



def run():
    """Runs the main program"""
    path_requested = request_path()

    # -------------------------------- Path check -------------------------------- #
    path = Path(path_requested)
    if check_is_correct_input(path):
        
        print('\n\n✨ Organizing your folder in a "organized" folder ✨')
        clean_folder(path)
        print('\t> ✅ Folder organized')
    else:
        print('\t> ❌ [ Error ] Incorrect path given')
