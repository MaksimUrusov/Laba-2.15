#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Написать программу, которая считывает из текстового файла три предложения и выводит их
в обратном порядке.
"""

if __name__ == "__main__":
    with open("ind.txt", "r") as txt:
        content = txt.readlines()[0:3]
        content.reverse()
        count = 0
        for line in content:
            print(line)