#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Написать программу, которая считывает текст из файла и выводит
# на экран только строки, не содержащие двузначных чисел.

import re


if __name__ == "__main__":
    with open("Lab_2.15/program/file_ind_1.txt", "r") as file: 
        text = file.readlines()
        result = []
        for line in text:
            if not re.search(r"\b\d{2}\b", line):
                result.append(line)
        print("".join(result))
