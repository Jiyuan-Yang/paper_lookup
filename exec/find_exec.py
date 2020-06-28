from utils.meta_params import get_db_list
from utils.output import find_result_print


def find_exec(args):
    name = args.name
    author = args.author
    tags = args.tags
    if name:
        name = name.split(';')
    if author:
        author = author.split(';')
    if tags:
        tags = tags.split(';')
    is_intersect = args.intersect
    is_union = args.union
    db_list = get_db_list()
    all_ok_list = []
    for item in db_list:
        ok = True
        item_id = item.get('id', None)
        item_name: str = item['items'].get('title', None)
        item_author: str = item['items'].get('author', None)
        item_tags: list = item.get('tags', None)
        item_tags_str: str = str(item_tags)
        if name:
            for name_part in name:
                if name_part.lower() not in item_name.lower() and is_intersect:
                    ok = False
                    break
                if name_part.lower() in item_name.lower() and is_union:
                    break
            if not ok:
                continue
        if author:
            for author_part in author:
                if author_part.lower() not in item_author.lower() and is_intersect:
                    ok = False
                    break
                if author_part.lower() in item_author.lower() and is_union:
                    break
            if not ok:
                continue
        if tags:
            for tags_part in tags:
                if tags_part.lower() not in item_tags_str.lower() and is_intersect:
                    ok = False
                    break
                if tags_part.lower() in item_tags_str.lower() and is_union:
                    break
            if not ok:
                continue
        all_ok_list.append([item_id, item_name, item_author, item_tags])
    find_result_print(all_ok_list, name=name, author=author, tags=tags)

