import os
import json
from configs.config_labels import l_root_path, l_shell_line_length

config_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.json')
db_file_name = 'db.json'


def get_root_path() -> str:
    with open(config_file_path) as f:
        return json.load(f)[l_root_path.get_name()]


def get_shell_line_length() -> int:
    with open(config_file_path) as f:
        return int(json.load(f)[l_shell_line_length.get_name()])


def get_db_list() -> list:
    with open(os.path.join(get_root_path(), db_file_name)) as f:
        return json.load(f)


def update_db_list(db_list: list) -> None:
    with open(os.path.join(get_root_path(), db_file_name), 'w') as f:
        json.dump(db_list, f, indent=2)
