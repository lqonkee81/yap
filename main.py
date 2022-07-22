#! /usr/bin/python3

'''
Написал: Усков Арсений
'''

import sys  # Для получения аргументов шелла

from Interpretor import Interpretor
from Formater import Formater

# Форматирование кода. Удаление комментариев и пустых строк
def format_code(input_file_path: str) -> str:
    with open(input_file_path, 'r') as code:
        code_from_file = code.readlines()

    formater = Formater(code_from_file)
    string = formater.formating()
    print(string)


def main() -> None:
    list_arguments = sys.argv   # Список 
    interpretor = Interpretor(list_arguments)

    if interpretor.is_args_validate():
        input_file_path = str()
        output_file_path = str()

        for i in range(1, len(list_arguments)):
            if list_arguments[i] == '-f':
                input_file_path = list_arguments[i + 1]
            if list_arguments[i] == '-o':
                output_file_path = list_arguments[i + 1]

        format_code(input_file_path)

    else:
        if len(list_arguments) == 1:
            print('Нужно указать файл')
        elif len(list_arguments) > 2 and len(list_arguments) < 5:
            print('Нужно указать либо только входной файл, либо входной файл через ключ -f и через ключ -о выходной файл')
        else:
            print('Ваще не понял, что ты хотел сделать')


if __name__ == '__main__':
    main()
