import re
import json
from utils.output import notify_print


def bib_parser(bib_string: str) -> dict:
    # use re.S flag to match more than one line
    basic_regexp = re.compile(r'@(?P<type>.*?){(?P<content>.*)}', re.S)
    basic_res = re.search(basic_regexp, bib_string)
    if not basic_res:
        notify_print('error', 'Invalid bib file.')
        exit(0)
    bib_type = basic_res.group('type')
    bib_content = basic_res.group('content').strip() + ',\n'
    content_regexp = re.compile(r'(?P<name>.*?),(?P<structured_content>.*)', re.S)
    content_res = re.search(content_regexp, bib_content)
    if not content_res:
        notify_print('error', 'Invalid bib content.')
        exit(0)
    bib_name = content_res.group('name')
    bib_structured_content = content_res.group('structured_content')
    # there should be '\s' after ','
    item_regexp = re.compile(r'\s*(?P<key>.*?)\s*=\s*{(?P<value>.*?)}\s*,\s', re.S)
    bib_item_dict = {}
    for item in re.finditer(item_regexp, bib_structured_content):
        if not item:
            notify_print('error', 'Invalid bib item.')
            exit(0)
        bib_item_dict[item.group('key')] = re.sub(r'\s+', ' ', item.group('value'))
    # print(bib_type)
    # print(bib_name)
    # print(bib_item_dict)
    bib_dict = {
        'type': bib_type,
        'name': bib_name,
        'items': bib_item_dict
    }
    return bib_dict


def bib_gen(bib_dict: dict) -> str:
    bib_file_str = '@' + bib_dict['type'] + '{' + bib_dict['name'] + ',\n'
    for item in bib_dict['items'].items():
        bib_file_str += item[0] + '={' + item[1] + '},\n'
    bib_file_str = bib_file_str[:-2] + '}'
    return bib_file_str


if __name__ == '__main__':
    print('>> test')
    a = """\
@article{vaswani2017attention,
title={Attention is All you Need},
author={Vaswani, Ashish and Shazeer, Noam and Parmar, Niki and Uszkoreit, Jakob and Jones, Llion and Gomez, Aidan N and Kaiser, Lukasz and Polosukhin, Illia},
pages={5998--6008},
year={2017}}
"""
    print(bib_parser(a))
    print(bib_gen(json.loads(bib_parser(a))))

