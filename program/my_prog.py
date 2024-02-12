#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os


if __name__ == "__main__":

    current_directory = os.getcwd()
    print(f"Текущая рабочая директория: {current_directory}")

    new_dir = "Lab_2.15/program/test_directory"
    os.mkdir(new_dir)
    print(f"Создана директория: {new_dir}")

    os.chdir(new_dir)
    print(f"Текущая рабочая директория изменена на: {os.getcwd()}")

    file_name = "test_file.txt"
    with open(file_name, 'w') as my_file:
        my_file.write("Привет, мир!")
    print(f"Создан файл: {file_name}")

    new_file_name = "renamed_file.txt"
    os.rename(file_name, new_file_name)
    print(f"Файл {file_name} переименован в {new_file_name}")
