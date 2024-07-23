import importlib.util
import os
from contextlib import contextmanager
from pathlib import Path

# def jls_extract_def():
#     custom_utils_path = Path('..', os.getcwd()).resolve() / 'custom_utils.py'
#     import_spec = importlib.spec_from_file_location(
#         'custom_utils', custom_utils_path)
#     custom_utils = importlib.module_from_spec(import_spec)
#     import_spec.loader.exec_module(custom_utils)
#     log_header = custom_utils.log_header
#     log = custom_utils.log
#     return log_header, log


@contextmanager
def load_module_from_path(module_name, path_to_file):
    spec = importlib.util.spec_from_file_location(module_name, path_to_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    yield module


def load_custom_utils():
    custom_utils_path = Path('..', os.getcwd()).resolve() / 'custom_utils.py'
    with load_module_from_path('custom_utils', custom_utils_path) as custom_utils:
        return custom_utils.log_header, custom_utils.log
