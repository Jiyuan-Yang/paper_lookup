import os
from utils.output import notify_print


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
