from core.config.meta_params import get_db_list
from core.utils.bib_parser import bib_gen


def export_exec(paper_id):
    for item in get_db_list():
        if item['id'] == paper_id:
            print(bib_gen(item))
            break
