import os
import json
from utils.output_methods import notify_print
from utils.input_methods import get_bool_choice, get_string_input
from configs.config_labels import l_root_path, l_shell_line_length
from configs.meta_params import config_file_path, db_file_name


def init_exec():
    if os.path.exists(config_file_path):
        if not get_bool_choice(
                'warning',
                'Configuration file already exists. Would you like to rewrite it?',
                default_choice=False
        ):
            return
    notify_print('info', 'Initializing configuration file.')

    root_path = l_root_path.get_type_transfer_func()(get_string_input(
        'Choose a folder to store the files (absolute path):\n',
        l_root_path.get_validation_check_func(),
        default_value=None
    ))

    shell_line_length = l_shell_line_length.get_type_transfer_func()(get_string_input(
        'Choose the length of line of your shell: ',
        l_shell_line_length.get_validation_check_func(),
        default_value='70'
    ))

    config_dict = {
        l_root_path.get_name(): root_path,
        l_shell_line_length.get_name(): shell_line_length
    }

    with open(config_file_path, 'w') as f:
        json.dump(config_dict, f, indent=2)

    if os.path.exists(os.path.join(root_path, 'bib_backup')):
        notify_print('warning', 'Folder \'bib_backup\' has already exists.')
    else:
        os.mkdir(os.path.join(root_path, 'bib_backup'))

    if os.path.exists(os.path.join(root_path, db_file_name)):
        notify_print('warning', f'File \'{db_file_name}\' has already exists.')
    else:
        with open(os.path.join(root_path, db_file_name), 'w') as f:
            json.dump([], f)

    notify_print('success', 'Initialization finished!')
