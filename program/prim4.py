#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    # open the fil2.txt in read mode. causes error if no such file exists.
    fileptr = open("Lab_2.15/program/file2.txt", "r")
    # stores all the data of the file into the variable content
    content = fileptr.readlines()
    # prints the content of the file
    print(content)
    # closes the opened file
    fileptr.close()