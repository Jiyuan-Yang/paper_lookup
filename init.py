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
        root_path = ''
        backup_path = ''
        while True:
            root_path = input('Choose a folder to store the files (absolute path):\n')
            if not os.path.exists(root_path):
                notify_print('error', 'Invalid path, try again.')
            else:
                notify_print('success', 'ROOT PATH has been successfully set.')
                break

        while True:
            backup_path = input('Choose a backup folder to backup all the files (eg. iCloud folder).'
                                'Press ENTER if you don\'t need to backup them:\n')
            if backup_path == '':
                notify_print('info', 'There will be no backup folder.')
                break
            else:
                if not os.path.exists(backup_path):
                    notify_print('error', 'Invalid path, try again.')
                else:
                    notify_print('success', 'BACKUP PATH has been successfully set.')
                    break
        config_dict = {
            'root_path': root_path,
            'backup_path': backup_path
        }
        with open(config_file_name, 'w') as f:
            json.dump(config_dict, f)
        notify_print('success', 'Initialization finished!')