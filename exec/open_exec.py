import os
import platform
from utils.meta_params import get_db_list, get_root_path
from utils.output import notify_print

os_mac = 0
os_windows = 1
os_linux = 2


def open_exec(args):
    paper_id = args.id
    for item in get_db_list():
        if item['id'] == int(paper_id):
            filename = item['filename']
            path = os.path.join(get_root_path(), filename)
            if get_os_info() == os_mac:
                os.system('open ' + path)
            elif get_os_info() == os_windows:
                os.system(path)
            else:
                notify_print('error', 'You have to set your own '
                                      'commend in exec/open_exec.py on Linux')
                exit(0)
            break


def get_os_info():
    pf_info = platform.system().lower()
    if 'darwin' in pf_info:
        return os_mac
    elif 'windows' in pf_info:
        return os_windows
    else:
        return os_linux
