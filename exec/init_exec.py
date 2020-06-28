import os
import json
from utils.output import notify_print
from utils.path_validation_check import check_root_path, check_backup_path
from utils.meta_params import config_file_name, db_file_name


def init_exec():
    if os.path.exists(config_file_name):
        # os.listdir().index(config_file_name)
        notify_print('warning', 'Configuration file already exists.')
    else:
        notify_print('info', 'Initializing configuration file.')

        while True:
            root_path = input('Choose a folder to store the files (absolute path):\n')
            if check_root_path(root_path):
                break

        while True:
            backup_path = input('Choose a backup folder to backup all the files (eg. iCloud folder).'
                                'Press ENTER if you don\'t need to backup them:\n')
            if check_backup_path(backup_path):
                break

        config_dict = {
            'root_path': root_path,
            'backup_path': backup_path
        }

        with open(config_file_name, 'w') as f:
            json.dump(config_dict, f, indent=2)

        os.mkdir(os.path.join(root_path, 'bib_backup'))
        with open(os.path.join(root_path, db_file_name), 'w') as f:
            json.dump([], f)
        notify_print('success', 'Initialization finished!')

