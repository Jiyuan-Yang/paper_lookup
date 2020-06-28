import os
import shutil
from utils.output import notify_print
from utils.meta_params import get_backup_path, get_root_path


def backup_exec():
    backup_path = get_backup_path()
    if not os.path.exists(backup_path):
        notify_print('error', 'Backup path do not exists.')
        exit(0)
    notify_print('info', 'Backing up files into {}'.format(backup_path))
    shutil.rmtree(get_backup_path())
    shutil.copytree(get_root_path(), get_backup_path())
    notify_print('success', 'Backup finished.')
