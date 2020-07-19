import os
from utils.output_methods import notify_print


def check_root_path(root_path):
    if not os.path.exists(root_path):
        notify_print('error', 'Invalid path, try again.')
        return False
    else:
        notify_print('success', 'root_path has been successfully set.')
        return True


def check_integer(input_str):
    try:
        _ = int(input_str)
        return True
    except ValueError:
        return False
