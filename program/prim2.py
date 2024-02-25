#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    # open the file.txt in write mode.
    fileptr = open("Lab_2.15/program/file2.txt", "a")
    # overwriting the content of the file
    fileptr.write(" Python has an easy syntax and user-friendly interaction.")
    # closing the opened file
    fileptr.close()
