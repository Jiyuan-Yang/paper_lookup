import json
from utils.output_methods import notify_print
from configs.meta_params import config_file_path
from configs.config_labels import l_shell_line_length, all_config_labels


def env_exec(arg_reset, arg_set):
    if not (arg_reset or arg_set):
        notify_print('error', 'There should be either --reset [env arg] '
                              'or --set [env arg] [new value]')
        exit(0)
    else:
        if arg_reset:
            could_be_reset = [l_shell_line_length.get_name()]
            if arg_reset not in could_be_reset:
                notify_print('error', f'{arg_reset} could not be reset')
                exit(0)
            else:
                with open(config_file_path) as f:
                    env_dict = json.load(f)
                    env_dict[arg_reset] = get_param_by_param_name(arg_reset) \
                        .get_default_value()
                with open(config_file_path, 'w') as f:
                    json.dump(env_dict, f, indent=2)
                notify_print('success', f'{arg_reset} has been reset')
        if arg_set:
            could_be_set = [l_shell_line_length.get_name()]
            if arg_set[0] not in could_be_set:
                notify_print('error', f'{arg_set[0]} could not be set')
                exit(0)
            else:
                param = get_param_by_param_name(arg_set[0])
                if not param.get_validation_check_func()(str(arg_set[1])):
                    notify_print('error', f'{arg_set[0]} could not be set')
                    exit(0)
                with open(config_file_path) as f:
                    env_dict = json.load(f)
                    env_dict[arg_set[0]] = param.get_type_transfer_func()(arg_set[1])
                with open(config_file_path, 'w') as f:
                    json.dump(env_dict, f, indent=2)
                notify_print('success', f'{arg_set[0]} has been set to {arg_set[1]}')


def get_param_by_param_name(param_name):
    return all_config_labels[[i.get_name() for i in all_config_labels].index(param_name)]
