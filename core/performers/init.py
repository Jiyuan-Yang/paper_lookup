import os
import json
from core.utils.print_function import notify_print
from core.utils.path_validation_check import check_root_path
from core.config.meta_params import config_file_name, db_file_name


def init_exec():
    if os.path.exists(config_file_name):
        while True:
            notify_print('warning',
                         'Configuration file already exists. '
                         'Would you like to rewrite it? [y/N]',
                         end='')
            choice = input()
            if choice == '' or choice == 'n' or choice == 'N':
                return
            elif choice == 'y' or choice == 'Y':
                break

    notify_print('info', 'Initializing configuration file.')

    while True:
        root_path = input('Choose a folder to store the files (absolute path):\n')
        if check_root_path(root_path):
            break

    config_dict = {
        'root_path': root_path,
    }

    with open(config_file_name, 'w') as f:
        json.dump(config_dict, f, indent=2)

    os.mkdir(os.path.join(root_path, 'bib_backup'))
    with open(os.path.join(root_path, db_file_name), 'w') as f:
        json.dump([], f)
    notify_print('success', 'Initialization finished!')
