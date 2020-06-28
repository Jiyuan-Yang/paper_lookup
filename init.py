import os
import json
from utils.output import notify_print

config_file_name = 'config.json'


def init_config():
    try:
        os.listdir().index(config_file_name)
        notify_print('warning', 'Configuration file already exists.')
    except ValueError:
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
        notify_print('success', 'Initialization finished!')


def check_root_path(root_path):
    if not os.path.exists(root_path):
        notify_print('error', 'Invalid path, try again.')
        return False
    else:
        notify_print('success', 'root_path has been successfully set.')
        return True


def check_backup_path(backup_path):
    if backup_path == '':
        notify_print('info', 'There will be no backup folder.')
        return True
    else:
        if not os.path.exists(backup_path):
            notify_print('error', 'Invalid path, try again.')
            return False
        else:
            notify_print('success', 'backup_path has been successfully set.')
            return True
