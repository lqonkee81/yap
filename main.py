#! /usr/bin/python3

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
    list_arguments = sys.argv                   # Список аргументов шелла
    interpretor = Interpretor(list_arguments)

    if not interpretor.is_args_validate():          # Проверка аргуметов на валидность
        print('Нужно указать только входной файл')
        quit()

    input_file_path = sys.argv[1]
    format_code(input_file_path)


if __name__ == '__main__':
    main()
