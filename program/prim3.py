#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    # open the file2.txt in read mode. causes error if no such file exists.
    fileptr = open("Lab_2.15/program/file2.txt", "r")
    # stores all the data of the file into the variable content
    content1 = fileptr.readline()
    content2 = fileptr.readline()
    # prints the content of the file
    print(content1)
    print(content2)
    # closes the opened file
    fileptr.close()