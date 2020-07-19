from utils.validation_check import check_root_path, check_shell_line_length


class ConfigLabel:
    def __init__(self, label_name, default_value,
                 validation_check_func, type_transfer_func=None):
        self.__label_name = label_name
        self.__default_value = default_value
        self.__validation_check_func = validation_check_func
        if type_transfer_func is None:
            self.__type_transfer_func = lambda x: x
        else:
            self.__type_transfer_func = type_transfer_func

    def get_name(self):
        return self.__label_name

    def get_default_value(self):
        return self.__default_value

    def get_validation_check_func(self):
        return self.__validation_check_func

    def get_type_transfer_func(self):
        return self.__type_transfer_func


l_root_path = ConfigLabel('root_path', '', check_root_path)
l_shell_line_length = ConfigLabel('shell_line_length', 70,
                                  check_shell_line_length, lambda x: int(x))

all_config_labels = [
    l_root_path,
    l_shell_line_length
]
