"""Deana Holmer"""
"""files-lab.py"""
import os
cwd=os.getcwd()
DATAINFILENAME=os.path.join(cwd,'students.txt')
DATAOUTFILENAME=os.path.join(cwd,'students.out')

with open(DATAINFILENAME,'r') as inf, open (DATAOUTFILENAME, 'w') as outf:
    students={}
    languages={}
    for each_line in inf:
        try:
            (name, langstr) = each_line.split(':',1)
            students[name]=langstr.split(',')
            for each_lang in students[name]:
                each_lang=each_lang.strip()
                if each_lang not in languages.keys():
                    languages.setdefault(each_lang, 1)
                else:
                    languages[each_lang] +=1
        except ValueError:
            if len(each_line) > 1:
                outf.write('#ValueError# ' + each_line)
    for name in students:
        outf.write(name + '\n')
        outf.write('\t' + str(students[name]) + '\n')

    for l in languages:
        print ('{}:\t{}'.format(l, languages[l]))


