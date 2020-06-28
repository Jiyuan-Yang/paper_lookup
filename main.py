import sys
import argparse
import json
from parsers.init_parser import init_parser
from parsers.env_parser import env_parser

parser = argparse.ArgumentParser(description='Paper Lookup, an easier way to manage your papers.')
# parser.add_argument('operation', default='', help='select an operation')
sub_parsers = parser.add_subparsers(help='sub parsers for Paper Lookup')

parser_init = sub_parsers.add_parser('init', help='initialize a configuration file')

parser_env = sub_parsers.add_parser('env', help='edit env arg')
parser_env.add_argument('-r', '--reset', help='reset an env arg')
parser_env.add_argument('-s', '--set', nargs=2, help='set [env arg] [new value]')

args = parser.parse_args()

sub_parser_name = sys.argv[1]

if sub_parser_name == 'init':
    init_parser()
elif sub_parser_name == 'env':
    env_parser(args, parser_env)

