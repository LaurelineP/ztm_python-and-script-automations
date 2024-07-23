import importlib.util
import os
import re
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
    print('spec', spec, module_name, path_to_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    yield module


def load_custom_utils():
    custom_utils_path = Path('..', os.getcwd()).resolve() / 'custom_utils.py'
    with load_module_from_path('custom_utils', custom_utils_path) as custom_utils:
        return custom_utils.log_header, custom_utils.log, custom_utils.log_object


def load_module(module_path: Path):
    module_name = module_path.name
    module_path_parent = module_path.parent

    print('module_name', module_name)
    print('module_path', module_path)

    with load_module_from_path(module_name, module_path) as _mod:
        attributes = list(filter(
            lambda attr: not re.search(r'^_', attr), dir(_mod))
        )
        print('attributes!', attributes)
        funcs = {}
        for exportable_name in attributes:
            func = _mod.__getattribute__(exportable_name)
            funcs[func.__name__] = func

        return funcs
