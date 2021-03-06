import sys
import argparse

from performers.init import init_exec
from performers.env import env_exec
from performers.load import import_exec
from performers.find import find_exec
from performers.open import open_exec
from performers.export import export_exec

from utils.output_methods import notify_print


parser = argparse.ArgumentParser(description='Paper Lookup, an easier way to manage your papers.')
parser.add_argument('-v', '--version', action='store_true', help='print version info')

sub_parsers = parser.add_subparsers(help='sub parsers for Paper Lookup')
parser_init = sub_parsers.add_parser('init', help='initialize a configuration file')
parser_env = sub_parsers.add_parser('env', help='edit env arg')
parser_import = sub_parsers.add_parser('import', help='import papers, paper and its bib file '
                                                      'should have the same name (eg. paper:'
                                                      ' some_paper.pdf, bib: some_paper.bib)')
parser_find = sub_parsers.add_parser('find', help='fetch info about papers, '
                                                  'use \';\' to add more keywords '
                                                  'and use \'\' to quote add the keywords')
parser_open = sub_parsers.add_parser('open', help='open paper')
parser_export = sub_parsers.add_parser('export', help='export bib files')

parser_env.add_argument('-r', '--reset', help='reset an env arg')
parser_env.add_argument('-s', '--set', nargs=2, help='set [env arg] [new value]')

parser_import.add_argument('-s', '--single', help='import single paper, -s [paper path]')
parser_import.add_argument('-f', '--folder', help='import all papers in a folder, -s [paper path]')
parser_import.add_argument('-t', '--tags', help='add tags for the papers, please use \';\'to'
                                                'split tags, and don\'t forget to use \'\' to'
                                                'quote the args')

parser_find.add_argument('-t', '--title', help='find by title')
parser_find.add_argument('-a', '--author', help='find by author')
parser_find.add_argument('-g', '--tags', help='find by tag')

parser_open.add_argument('id', help='the id of paper to open')

parser_export.add_argument('id', help='the id of paper to export the corresponding bib file')

args = parser.parse_args()

if len(sys.argv) <= 1:
    notify_print('error', 'Invalid command.')
    parser.print_help()
    exit(0)

sub_parser_name = sys.argv[1]

if sub_parser_name == 'init':
    init_exec()
elif sub_parser_name == 'env':
    env_exec(args.reset, args.set)
elif sub_parser_name == 'import':
    import_exec(args.folder, args.single, args.tags)
elif sub_parser_name == 'find':
    find_exec(args.title, args.author, args.tags)
elif sub_parser_name == 'open':
    open_exec(int(args.id))
elif sub_parser_name == 'export':
    export_exec(int(args.id))
else:
    if args.version:
        print('Paper Lookup version 1.0.0')
    else:
        notify_print('error', 'Invalid command.')
        parser.print_help()
