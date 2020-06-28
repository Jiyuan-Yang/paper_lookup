from colorama import Fore, Style

type_dict = {
    'info': '➡️',
    'warning': '⚠️',
    'error': '❌',
    'success': '✅',
}

type_dict_plain = {
    'info': Fore.BLUE + 'info' + Style.RESET_ALL,
    'warning': Fore.YELLOW + 'warning' + Style.RESET_ALL,
    'error': Fore.RED + 'error' + Style.RESET_ALL,
    'success': Fore.GREEN + 'success' + Style.RESET_ALL,
}

notify_template = '{type} {message}'
notify_template_plain = '[{type}] {message}'


def notify_print(notify_type, message, use_plain=True):
    type_d = type_dict if not use_plain else type_dict_plain
    template = notify_template if not use_plain else notify_template_plain
    print(template.format(
        type=type_d[notify_type],
        message=message
    ))
