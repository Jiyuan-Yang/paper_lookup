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


def notify_print(notify_type, message, use_plain=True, end='\n'):
    type_d = type_dict if not use_plain else type_dict_plain
    template = notify_template if not use_plain else notify_template_plain
    print(template.format(
        type=type_d[notify_type],
        message=message
    ), end=end)


def find_result_print(find_result_list: list):
    print(' {:4} | {:25} | {:15} | {:15} '.format('id', 'title', 'author', 'tags'))
    for item in find_result_list:
        item_id, item_title, item_author, item_tags = item
        item_title = chop_max_len(item_title, 25)
        item_author = chop_max_len(item_author, 15)
        item_tags = chop_max_len(';'.join(item_tags), 15)
        print(' {:4} | {:25} | {:15} | {:15} '.format(
            item_id, item_title, item_author, item_tags))


def chop_max_len(string: str, max_len: int) -> str:
    if len(string) <= max_len:
        return string
    else:
        new_str = list(string[:max_len])
        new_str[-3:] = ['.'] * 3
        return ''.join(new_str)
