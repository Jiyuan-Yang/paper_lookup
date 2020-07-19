import os
from utils.output_methods import notify_print


def check_root_path(root_path: str) -> bool:
    if not os.path.exists(root_path):
        notify_print('error', 'Invalid path, try again.')
        return False
    else:
        notify_print('success', f'root_path has been successfully set.')
        return True


def check_shell_line_length(input_str: str) -> bool:
    if not check_integer(input_str):
        return False
    else:
        if int(input_str) < 30:
            notify_print('error', f'shell_line_length should '
                                  f'be equal or greater than 30.')
            return False
        else:
            notify_print('success', f'shell_line_length has '
                                    f'been successfully set.')
            return True


def check_integer(input_str):
    try:
        _ = int(input_str)
        return True
    except ValueError:
        return False
