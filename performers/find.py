from configs.meta_params import get_db_list, get_shell_line_length
from utils.output_methods import find_result_print
from utils.parser.condition_parser import condition_check


def find_exec(title, author, tags):
    db_list = get_db_list()
    all_ok_list = []
    for item in db_list:
        item_id = item.get('id', None)
        item_name = item['items'].get('title', None)
        item_author = item['items'].get('author', None)
        item_tags = item.get('tags', None)
        item_tags_str = str(item_tags)
        if title and not condition_check(item_name, title):
            continue
        if author and not condition_check(item_author, author):
            continue
        if tags and not condition_check(item_tags_str, tags):
            continue
        all_ok_list.append([item_id, item_name, item_author, item_tags])
    find_result_print(all_ok_list, get_shell_line_length())
