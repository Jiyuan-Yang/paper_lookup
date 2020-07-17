from core.config.meta_params import get_db_list
from core.utils.print_function import find_result_print


def find_exec(name, author, tags, is_intersect, is_union):
    if name:
        name = name.split(';')
    if author:
        author = author.split(';')
    if tags:
        tags = tags.split(';')
    # print(name, author, tags)
    db_list = get_db_list()
    all_ok_list = []
    for item in db_list:
        item_id = item.get('id', None)
        item_name: str = item['items'].get('title', None)
        item_author: str = item['items'].get('author', None)
        item_tags: list = item.get('tags', None)
        item_tags_str: str = str(item_tags)
        if not find_judge(name, item_name, is_union):
            continue
        if not find_judge(author, item_author, is_union):
            continue
        if not find_judge(tags, item_tags_str, is_union):
            continue
        all_ok_list.append([item_id, item_name, item_author, item_tags])
    find_result_print(all_ok_list, name=name, author=author, tags=tags)


def find_judge(all_kw: None or list, item: str, is_union: bool) -> bool:
    ok = True
    if all_kw:
        if is_union:
            has_at_least_one = False
            for kw in all_kw:
                if kw.lower() in item.lower():
                    has_at_least_one = True
                    break
            if not has_at_least_one:
                ok = False
        else:
            # default is intersect
            for kw in all_kw:
                if kw.lower() not in item.lower():
                    ok = False
                    break
    return ok
