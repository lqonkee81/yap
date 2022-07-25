from Formater import Formater


class Interpretor:
    def __init__(self, list_arguments: list) -> None:
        self.list_arguments = list_arguments

    def doc(self):
        '''
        Кто-то должен написать документацию
        '''

    # Валидатор аргументов шелла
    def is_args_validate(self) -> bool:
        if len(self.list_arguments) == 1:
            self.doc()
            quit()

        elif len(self.list_arguments) == 2:
            return True
        else:
            return False
