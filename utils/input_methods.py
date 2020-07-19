from utils.output_methods import notify_print


def get_bool_choice(notify_type, message, default_choice=False) -> bool:
    # default_choice: True for Yes, False for No
    if default_choice:
        message += ' [Y/n]'
    else:
        message += ' [y/N]'
    while True:
        notify_print(notify_type, message, end='')
        choice = input().strip()
        if default_choice:
            if choice == '' or choice.lower() == 'y':
                return True
            elif choice.lower() == 'n':
                return False
        else:
            if choice == '' or choice.lower() == 'n':
                return False
            elif choice.lower() == 'y':
                return True


def get_string_input(message, validation_function, default_value: None or str) -> str:
    while True:
        if default_value is not None:
            message += f' [default: {default_value}]'
        user_input = input(message).strip()
        if user_input == '':
            return default_value
        if validation_function(user_input):
            return user_input
