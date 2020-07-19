import json
from utils.output_methods import notify_print
from config.meta_params import config_file_path


def env_exec(arg_reset, arg_set):
    if not (arg_reset or arg_set):
        notify_print('error', 'There should be either --reset [env arg] '
                              'or --set [env arg] [new value]')
        exit(0)
    else:
        if arg_reset:
            could_be_reset = []
            # TODO: Add more environment args
            if arg_reset not in could_be_reset:
                notify_print('error', f'{arg_reset} could not be reset')
                exit(0)
            else:
                with open(config_file_path) as f:
                    env_dict = json.load(f)
                    env_dict[arg_reset] = ''
                with open(config_file_path, 'w') as f:
                    json.dump(env_dict, f, indent=2)
                notify_print('success', f'{arg_reset} has been reset')
        if arg_set:
            could_be_set = []
            if arg_set[0] not in could_be_set:
                notify_print('error', f'{arg_set[0]} could not be set')
                exit(0)
            else:
                # TODO: Add more environment args
                if True:
                    pass
                else:
                    notify_print('error', f'{arg_set[0]} could not be set')
                    exit(0)
                with open(config_file_path) as f:
                    env_dict = json.load(f)
                    env_dict[arg_set[0]] = arg_set[1]
                with open(config_file_path, 'w') as f:
                    json.dump(env_dict, f, indent=2)
                notify_print('success', f'{arg_set[0]} has been set to {arg_set[1]}')
