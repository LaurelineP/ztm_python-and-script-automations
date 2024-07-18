from pathlib import Path
from shutil import copy, move, rmtree

from custom_utils import log_header


print('\n\n\n')
log_header('02. Path and Folders', False)
print(' --- cleaning folder and files')
print('\n\n\n')


def display_paths_details():
    """Displays details from this current"""
    log_header('display_paths_details')
    folders = {
        "current": Path('.'),
        "home": Path.home(),
    }
    print("\tcurrent:", folders["current"])
    print("\thome:", folders["home"])

    accessed_home_downloads = folders['home'] / 'Downloads'
    print("\taccessed home download folder:", accessed_home_downloads)


def display_paths_details_2():
    """Deeper pathlib details"""
    log_header('display_paths_details_2')
    this = {
        "get_parent": lambda: Path('.').parent,
        "does_exist": lambda path: Path(path).exists(),
        "get_info": lambda path: Path(path).stat()
    }
    print('\tThis get parent (parent):', this["get_parent"]())
    print('\tThis does exist (exists):', this["does_exist"]('./__pycache__'))
    print('\tInfos (stat):', this["get_info"]('./__pycache__'))


def iter_over_directory(path):
    """Iterate over the folder to ease the navigation through a given path"""
    log_header('iter_over_directory')
    iter_content = Path(path).iterdir()
    print('\tpath dir iteration content (iterdir):', iter_content)
    for x in iter_content:
        """Displays info for file or folder using pathlib Path properties and methods"""
        is_file = x.is_file()
        is_dir = x.is_dir()
        file_or_folder = x.name
        file_or_folder_no_ext = x.stem

        is_file and print('\t--> 📃 is file:', x.name, 'of type')
        is_dir and print('\t--> 🗂️ is directory:', x.name, 'of type')


def manage_folder_and_files(action, path, target=""):
    """Takes action on file or folder ( copy, rename, paste, delete )
            Following details the different options: benefits and inconvenient
    """
    log_header('manage_folder_and_files')
    print('action:', action)

    origin_path = Path(path)
    # related to current folder
    destination_path = Path(__file__) \
        .absolute().parent/target
    # ------------------------------- CREATE FOLDER ------------------------------ #
    if action == 'create':

        # Creates directory: OK if does not exist, if exists --> raise error
        # _path.mkdir()

        # Create a directory: OK if does not exist, if exists --> error raised prevented - non nested
        # _path.mkdir(exist_ok=True)

        # Create a directory: NOK if does not exist - nested
        __path = origin_path / 'fake1' / 'fake2'
        # _path.mkdir(exist_ok=True)

        __path.mkdir(exist_ok=True, parents=True)

        if __path.exists():
            print(f'Created folder:{__path}')

    # --------------------------------- COPY FILE -------------------------------- #
    elif action == 'copy':

        # shutil.copy
        copy(origin_path, destination_path)
        print('origin_path', origin_path)
        print('destination_path', destination_path)
        if destination_path.exists():
            print(f'Copied file in {destination_path}')

    # --------------------------------- RENAMING --------------------------------- #
    elif action == 'rename':
        move(origin_path, destination_path)
        if destination_path.exists():
            print(f'Renamed file in {destination_path}')

    elif action == 'delete':
        # sample: ensure to have a folder path
        file_or_folder_to_remove = Path(path)
        print('--> path', file_or_folder_to_remove)

        # mere & quick check if file or folder based on extension syntax after `.`
        splitted_path = str(file_or_folder_to_remove).split('.')
        is_file = len(splitted_path) > 1

        # describes the exact content ( file | folder )
        content = 'file' if is_file else 'folder'

        # sample: ensures to have a folder to remove
        if not file_or_folder_to_remove.exists() and not is_file:
            file_or_folder_to_remove.mkdir(exist_ok=True, parents=True)
        elif not file_or_folder_to_remove.exists() and is_file:
            file_or_folder_to_remove.touch()

        # remove  handler - depending on file ( unlink ) or folder ( rmdir )
        remove_handler = file_or_folder_to_remove.unlink if is_file else file_or_folder_to_remove.rmdir
        remove_handler()

        # feedback: state the removal success or failure
        if not file_or_folder_to_remove.exists():
            print(
                f'Removed successfully the {content}: \n\t{file_or_folder_to_remove}'
            )

    else:
        print('Unknown manage_folder_and_files action')
