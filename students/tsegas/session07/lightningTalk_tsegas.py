#
# This script takes a files and changes a specified line in that files by finding a
# string in the line and changing it in place. It also backs up the original files content.

import os
import sys

# This function takes an input file and changes a specified line in that files and it
# also backs up the original files content
def change_string(filename, bachup_file, old_string, new_string):
	datafile= filename
	try:
		 with open(datafile) as f: print("looking for file...")
	except IOError as e:
		print("Error: %s not found." % datafile)
		return

	os.rename(filename,bachup_file)
	f1 = open(bachup_file, 'r')
	f2 = open(filename, 'w')
	for line in f1:
		if "component character_decoder is" in line:
			print("the line that was found:",line)
			f2.write(line)
			f2.write('      ' +next(f1, '').strip().replace(old_string, new_string) + '\n')
		else:
			f2.write(line)
	f1.close()
	f2.close()
fname = input('enter filename?:')
back_fname = input('enter backup filename?:')
ostring = input('enter old string?:')
nstring = input('enter new string?:')
#call function change_string with the file specific parameters
change_string(filename=fname,bachup_file=back_fname,old_string=ostring,new_string=nstring)
#change_string(filename='data.txt',bachup_file='data_back.txt',old_string="integer := 40_000_000",new_string="integer := 20_000_000")
#