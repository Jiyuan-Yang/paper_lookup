import os
import json

config_file_name = os.path.join(os.path.abspath(os.curdir), 'config.json')
db_file_name = 'db.json'


def get_root_path() -> str:
    with open(config_file_name) as f:
        return json.load(f)['root_path']


def get_backup_path() -> str:
    with open(config_file_name) as f:
        return json.load(f)['backup_path']


def get_db_list() -> list:
    with open(os.path.join(get_root_path(), db_file_name)) as f:
        return json.load(f)


def update_db_list(db_list: list) -> None:
    with open(os.path.join(get_root_path(), db_file_name), 'w') as f:
        json.dump(db_list, f, indent=2)
