'''
Написал: Усков Арсений
'''

from Formater import Formater


class Interpretor:
    def __init__(self, list_arguments: list) -> None:
        self.list_arguments = list_arguments

    # Проверка парамеров шелла на валидность
    def is_args_validate(self) -> bool:
        if len(self.list_arguments) == 5 or len(self.list_arguments) == 2:
            return True
        else:
            return False
