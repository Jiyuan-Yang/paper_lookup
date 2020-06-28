import sys
import argparse
from exec.init_exec import init_exec
from exec.env_exec import env_exec
from exec.import_exec import import_exec
from utils.output import notify_print

parser = argparse.ArgumentParser(description='Paper Lookup, an easier way to manage your papers.')
parser.add_argument('-v', '--version', action='store_true', help='print version info')

sub_parsers = parser.add_subparsers(help='sub parsers for Paper Lookup')

parser_init = sub_parsers.add_parser('init', help='initialize a configuration file')

parser_env = sub_parsers.add_parser('env', help='edit env arg')
parser_env.add_argument('-r', '--reset', help='reset an env arg')
parser_env.add_argument('-s', '--set', nargs=2, help='set [env arg] [new value]')

parser_import = sub_parsers.add_parser('import', help='import papers, paper and its bib file '
                                                      'should have the same name (eg. paper:'
                                                      ' some_paper.pdf, bib: some_paper.bib)')
parser_import.add_argument('-s', '--single', help='import single paper, -s [paper path]')
parser_import.add_argument('-f', '--folder', help='import all papers in a folder, -s [paper path]')
parser_import.add_argument('-t', '--tags', help='add tags for the papers, tags should not '
                                                'contain space, you could use \'-\' to'
                                                'replace the space and please use \';\'to'
                                                'split tags.')
parser_import.add_argument('-nb', '--no-bib', action='store_true',
                           help='if there is no bib file, use this flag')

args = parser.parse_args()

sub_parser_name = sys.argv[1]

if sub_parser_name == 'init':
    init_exec()
elif sub_parser_name == 'env':
    env_exec(args, parser_env)
elif sub_parser_name == 'import':
    import_exec(args)
else:
    if args.version:
        print('Paper Lookup version 1.0.0')
    else:
        notify_print('error', 'Invalid command.')
        parser.print_help()
