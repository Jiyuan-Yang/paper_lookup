import os
import json
from utils.output_methods import notify_print
from utils.validation_check import check_root_path, check_integer
from config.meta_params import config_file_path, db_file_name
from utils.input_methods import get_bool_choice, get_string_input


def init_exec():
    if os.path.exists(config_file_path):
        if not get_bool_choice(
                'warning',
                'Configuration file already exists. Would you like to rewrite it?',
                default_choice=False
        ):
            return
    notify_print('info', 'Initializing configuration file.')

    root_path = get_string_input(
        'Choose a folder to store the files (absolute path):\n',
        check_root_path,
        default_value=None
    )

    shell_line_length = int(get_string_input(
        'Choose the length of line of your shell: ',
        check_integer,
        default_value='70'
    ))

    config_dict = {
        'root_path': root_path,
        'shell_line_length': shell_line_length
    }

    with open(config_file_path, 'w') as f:
        json.dump(config_dict, f, indent=2)

    if os.path.exists(os.path.join(root_path, 'bib_backup')):
        notify_print('warning', 'Folder \'bib_backup\' has already exists.')
    else:
        os.mkdir(os.path.join(root_path, 'bib_backup'))

    if os.path.exists(os.path.join(root_path, db_file_name)):
        notify_print('warning', f'File \'#{db_file_name}\' has already exists.')
    else:
        with open(os.path.join(root_path, db_file_name), 'w') as f:
            json.dump([], f)

    notify_print('success', 'Initialization finished!')
