#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Написать программу, которая считывает текст из файла и определяет, сколько в нем слов,
состоящих из не менее чем семи букв.
"""


if __name__ == "__main__":
    with open("ind_1.txt", "r", encoding="utf-8") as fileptr:
        puncList = [".", ";", ":", "!", "?", "/", ",", ")", "(", "\"", "\n"]
        text = fileptr.read()
        for i in text:
            if i in puncList:
                text = text.replace(i, "")
        words = text.split(" ")

        s = len([word for word in words if len(word) > 6])
        print(f"Количество слов, состоящих из не менее 7 букв: {s}")