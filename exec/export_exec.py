from utils.meta_params import get_db_list
from utils.bib_utils import bib_gen


def export_exec(args):
    paper_id = int(args.id)
    for item in get_db_list():
        if item['id'] == paper_id:
            print(bib_gen(item))
            break
