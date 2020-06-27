type_dict = {
    'info': '➡️',
    'warning': '⚠️',
    'error': '❌',
    'success': '✅',
}

type_dict_plain = {
    'info': '\033[34minfo\033[0m',
    'warning': '\033[33mwarning\033[0m',
    'error': '\033[31merror\033[0m',
    'success': '\033[32msuccess\033[0m',
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
