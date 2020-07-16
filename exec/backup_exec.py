import os
import shutil
from colorama import Fore, Style
from utils.output import notify_print
from utils.meta_params import get_backup_path, get_root_path


def backup_exec():
    backup_path = get_backup_path()
    if not os.path.exists(backup_path):
        notify_print('error', 'Backup path do not exists.')
        exit(0)
    notify_print('info', 'Backing up files into {}'.format(backup_path))
    notify_print('error', 'Backup module has been deprecated.')
    exit(0)
    if os.path.exists(get_backup_path()):
        while True:
            user_choice = input(Fore.RED + 'We are going to REMOVE this folder: {}, continue [y/N]?'
                                .format(get_backup_path()) + Style.RESET_ALL)
            if user_choice == '' or user_choice == 'n' or user_choice == 'N':
                notify_print('error', 'Backup was interrupted by user.')
                exit(0)
            elif user_choice == 'y' or user_choice == 'Y':
                break
        shutil.rmtree(get_backup_path())
    shutil.copytree(get_root_path(), get_backup_path())
    notify_print('success', 'Backup finished.')
