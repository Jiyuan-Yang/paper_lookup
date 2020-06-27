import argparse
from init import init_config


cmd_parser = argparse.ArgumentParser(description='Paper Lookup, an easier way to manage your papers.')
cmd_parser.add_argument('operation', default='', help='select an operation')
cmd_parser.add_argument('other', nargs=argparse.REMAINDER)

args = cmd_parser.parse_args()
operation = args.operation


if operation == 'init':
    init_config()
elif operation == 'env':
    pass