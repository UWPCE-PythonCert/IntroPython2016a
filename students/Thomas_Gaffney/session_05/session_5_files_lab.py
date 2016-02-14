# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 22:12:54 2016

@author: tom.gaffney
"""

language_list = []
dict_of_languages ={}
with open('students.txt', 'r') as f:
    for line in f:
        colon_sep = line.rstrip().split(':')
        languages = colon_sep[1].split(',')
        for language in languages:
            try: dict_of_languages[language] = dict_of_languages[language]+1
            except: dict_of_languages[language] = 1
        language_list.extend(languages)

languages = list(set(language_list))
print(languages)
