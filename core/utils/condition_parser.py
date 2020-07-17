def condition_check(string: str, condition: str) -> bool:
    condition = chop_redundant_bracket(condition.strip()).strip()
    level_dict = get_level_dict(condition)
    if level_dict == {}:
        return has_sub_string(string, condition)
    else:
        min_level = min(level_dict.keys())
        min_level_dict = level_dict[min_level]
        if min_level_dict['|']:
            check_left = condition_check(string, condition[0:min_level_dict['|'][0]])
            if check_left:
                return True
            check_right = condition_check(string, condition[min_level_dict['|'][0] + 1:])
            return check_right
        else:
            check_left = condition_check(string, condition[0:min_level_dict['&'][0]])
            if not check_left:
                return False
            check_right = condition_check(string, condition[min_level_dict['&'][0] + 1:])
            return check_right


def get_level_dict(condition: str) -> dict:
    current_level = 0
    level_dict = {}
    for idx, ch in enumerate(condition):
        if ch == '(':
            current_level += 1
        elif ch == ')':
            current_level -= 1
        elif ch == '&' or ch == '|':
            current_level_dict = level_dict.get(current_level, None)
            if not current_level_dict:
                level_dict[current_level] = {'&': [], '|': []}
                current_level_dict = level_dict[current_level]
            if ch == '&':
                current_level_dict['&'].append(idx)
            else:
                current_level_dict['|'].append(idx)
    return level_dict


def has_sub_string(string: str, sub_string: str) -> bool:
    try:
        _ = string.index(sub_string)
        return True
    except ValueError:
        return False


def chop_redundant_bracket(string: str) -> str:
    while True:
        check, left_or_right = has_right_level(string)
        if check:
            break
        elif left_or_right == 0:
            string = string[1:]
        else:
            string = string[:-1]
    while True:
        if len(string) > 2 and string[0] == '(' and string[-1] == ')':
            string = string[1:-1]
        else:
            return string


def has_right_level(string: str) -> (bool, int or None):
    # 0 for left, 1 for right
    level = 0
    for ch in string:
        if ch == '(':
            level += 1
        elif ch == ')':
            level -= 1
    if level == 0:
        return True, None
    elif level > 0:
        return False, 0
    else:
        return False, 1


if __name__ == '__main__':
    pass
