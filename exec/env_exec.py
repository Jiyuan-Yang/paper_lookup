import json
from utils.output import notify_print
from utils.path_validation_check import check_backup_path
from utils.meta_params import config_file_name


def env_exec(args, parser_env):
    arg_reset = args.reset
    arg_set = args.set
    if not (arg_reset or arg_set):
        notify_print('error', 'There should be either --reset [env arg] '
                              'or --set [env arg] [new value]')
        parser_env.print_help()
        exit(0)
    else:
        if arg_reset:
            could_be_reset = ['backup_path']
            if arg_reset not in could_be_reset:
                notify_print('error', f'{arg_reset} could not be reset')
                exit(0)
            else:
                with open(config_file_name) as f:
                    env_dict = json.load(f)
                    env_dict[arg_reset] = ''
                with open(config_file_name, 'w') as f:
                    json.dump(env_dict, f, indent=2)
                notify_print('success', f'{arg_reset} has been reset')
        if arg_set:
            could_be_set = ['backup_path']
            if arg_set[0] not in could_be_set:
                notify_print('error', f'{arg_set[0]} could not be set')
                exit(0)
            else:
                if arg_set[0] == 'backup_path':
                    if not check_backup_path(arg_set[1]):
                        notify_print('error', f'{arg_set[1]} is not a valid path')
                        exit(0)
                else:
                    notify_print('error', f'{arg_set[0]} could not be set')
                    exit(0)
                with open(config_file_name) as f:
                    env_dict = json.load(f)
                    env_dict[arg_set[0]] = arg_set[1]
                with open(config_file_name, 'w') as f:
                    json.dump(env_dict, f, indent=2)
                notify_print('success', f'{arg_set[0]} has been set to {arg_set[1]}')
