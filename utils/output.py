type_dict = {
    'info': '📢️',
    'warning': '⚠️',
    'error': '❌',
    'success': '✅',
}

type_dict_plain = {
    'info': 'info',
    'warning': 'warning',
    'error': 'error',
    'success': 'success',
}

notify_template = '{type} {message}'
notify_template_plain = '[{type}] {message}'


def notify_print(notify_type, message, use_plain=False):
    type_d = type_dict if not use_plain else type_dict_plain
    template = notify_template if not use_plain else notify_template_plain
    print(template.format(
        type=type_d[notify_type],
        message=message
    ))
