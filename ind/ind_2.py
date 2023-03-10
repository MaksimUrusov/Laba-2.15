#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите программу, которая будет считывать список слов из
файла и собирать статистику о том, в каком проценте слов используется каждая буква
алфавита. Выведите результат для всех 26 букв английского алфавита и отдельно отметьте
букву, которая встречалась в словах наиболее редко. В вашей программе должны
игнорироваться знаки препинания и регистр символов.
"""


if __name__ == "__main__":
    with open("ind_2.txt", "r", encoding="utf-8") as fileptr:
        english = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                   "n", "o", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        puncList = [".", ";", ":", "!", "?", "/", ",", ")", "(", "\"", "\n"]

        text = fileptr.read().lower()
        for i in text:
            if i in puncList:
                text = text.replace(i, "")
        words = text.split(" ")

        n = len(words)
        minper = n
        minl = ""

        for letter in english:
            s = sum([1 for word in words if letter in word])
            if s < minper:
                minl = letter
            print(f"Letter {letter} is present in {s/n*100:.2f}% words\n")
        print(f"Letter {minl} is the least common")