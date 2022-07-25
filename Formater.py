class Formater:
    '''
    Модуль, который занимается форматированием файла, перед его исполнением. Сначала он удаляет комментарии.
    За комментарии считаются:
        1. строки, начинающиеся с #
        2. строки, обрамленные в #
    '''

    def __init__(self, code_from_file: str):
        self.__code_from_file = code_from_file
        self.comment_char = '#'

    # =====> Удаление комментариев
    def __remove_comments(self, input_code: list) -> list:
        '''
        Получает на вход список со строками из .yp файла.
        Далее удаляет комментарии
        '''
        fr_code = list()

        for code_string in input_code:
            flag = False
            tmp_str = ''

            for i in range(0, len(code_string)):
                if code_string[i] == self.comment_char:
                    if not flag:
                        flag = True
                    else:
                        flag = False
                        continue
                if not flag:
                    tmp_str += code_string[i]
            tmp_str = tmp_str.strip()
            fr_code.append(tmp_str)

        return fr_code

    # =====> Удаление пустых строк
    def __remove_empty_rows(self, input_code: list) -> list:
        fr_code = list()

        for i in input_code:
            if i != '\n' and i != '':
                fr_code.append(i)

        return fr_code

    # =====> Форматирование строки
    def formating(self):
        self.__code_after_del_coms = self.__remove_comments(self.__code_from_file)
        self.__code_after_rem_emp_rows = self.__remove_empty_rows(self.__code_after_del_coms)

        return self.__code_after_rem_emp_rows
