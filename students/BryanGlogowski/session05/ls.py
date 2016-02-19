#!/usr/bin/env python3

import os

def get_file_list(path):
    """Returns a list of absolute paths"""
    return [os.path.join(os.getcwd(),f) for f in os.listdir('.')]

def print_list(files):
    """Prints the items in a list"""
    for file in files:
        print(file)

def list_all_files(path):
    """Gets a list of files and prints them"""
    print_list(get_file_list(path))

list_all_files('.')

