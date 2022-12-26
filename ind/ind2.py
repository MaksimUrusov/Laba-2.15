#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
В операционных системах на базе Unix обычно присутствует утилита с названием head.
Она выводит первые десять строк содержимого файла, имя которого передается в качестве
аргумента командной строки. Напишите программу на Python, имитирующую поведение
этой утилиты. Если файла, указанного пользователем, не существует, или не задан аргумент командной строки,
необходимо вывести соответствующее сообщение об
ошибке.
"""


import sys
import os.path


if __name__ == "__main__":
    n = int(input("Input count of lines "))
    if n == "":
        raise TypeError("Wrong type - input number")
    check = os.path.exists(sys.argv[1])
    if check:
        with open(sys.argv[1], "r") as txt:
            content = txt.readlines()
            for line in content:
                print(line)
    else:
        raise ExistError("File not exist or not set argument")