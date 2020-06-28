import os
import shutil
from utils.output import notify_print
from utils.meta_params import get_root_path, get_db_list, update_db_list
from utils.bib_utils import bib_parser


def import_exec(args):
    db_list = get_db_list()
    id_cnt = len(db_list)
    no_bib = args.no_bib  # set --no-bib flag to eliminate warnings
    folder = args.folder
    single = args.single
    tags = args.tags
    root_path = get_root_path()
    if not (folder or single):
        notify_print('error', 'Please set either a folder or a single file to import')
        exit(0)
    if no_bib:
        notify_print('warning', '--no-bib flag has been set, there will be no more '
                                'warnings about the absent bib files')
        notify_print('warning', 'bib file is important to keep the info of a paper, '
                                'and we use bib file to search papers in the local database. '
                                'Therefore, we do NOT recommend to use this flag.')
    if not os.path.exists(root_path):
        notify_print('error', 'Folder at root path does not exist.')
        exit(0)
    if folder:
        if not os.path.exists(folder):
            notify_print('error', 'Folder does not exist.')
            exit(0)
        for file in os.listdir(folder):
            if os.path.splitext(file)[-1] == '.bib':
                continue
            bib_dict = import_single(folder, file, root_path)
            if not bib_dict:
                continue
            bib_dict['id'] = id_cnt
            id_cnt += 1
            bib_dict['tags'] = []
            if tags:
                bib_dict['tags'] = tags.split(';')
            db_list.append(bib_dict)
    if single:
        single_folder, single_file = os.path.split(single)
        bib_dict = import_single(single_folder, single_file, root_path)
        if not bib_dict:
            return
        bib_dict['id'] = id_cnt
        id_cnt += 1
        bib_dict['tags'] = []
        if tags:
            bib_dict['tags'] = tags.split(';')
        db_list.append(bib_dict)
    update_db_list(db_list)


def import_single(folder: str, file: str, root_path: str) -> dict or None:
    if os.path.splitext(file)[-1] != '.pdf' and os.path.splitext(file)[-1] != '.bib':
        notify_print('warning', f'File/folder {file} is neither a PDF file '
                                f'nor a BIB file, thus it has been ignored.')
        return None
    notify_print('info', f'Importing {file}')
    bib_path = os.path.join(folder, os.path.splitext(file)[0] + '.bib')
    if not os.path.exists(bib_path):
        notify_print('warning', f'File {file} does not have a corresponding bib file.')
        notify_print('warning', f'Using the original file name {file}.')
        shutil.copy(os.path.join(folder, file), os.path.join(root_path, file))
        return None
    else:
        with open(bib_path) as f:
            bib_dict = bib_parser(f.read())
            name: str = bib_dict['name']
            title: str = bib_dict['items'].get('title', None)
            if title:
                title = title.strip().replace(' ', '-')
                notify_print('info', f'Using title {title} as the new file name.')
                shutil.copy(os.path.join(folder, file),
                            os.path.join(root_path, title + os.path.splitext(file)[-1]))
            elif name:
                name = name.strip().replace(' ', '-')
                notify_print('info', f'Using name {name} as the new file name.')
                shutil.copy(os.path.join(folder, file),
                            os.path.join(root_path, name + os.path.splitext(file)[-1]))
            else:
                notify_print('warning', f'Using the original file name {file}.')
                shutil.copy(os.path.join(folder, file), os.path.join(root_path, file))
            return bib_dict
