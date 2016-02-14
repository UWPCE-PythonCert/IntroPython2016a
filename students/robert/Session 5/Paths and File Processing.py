#!/usr/bin/python


#Find and print file locations
import pathlib  
pth = pathlib.Path('./')
abpth = pth.absolute()
for fn in pth.iterdir():
    print(str(abpth) + '\\' + str(fn))

# Copy file to designated location
file_name = input ('file_name with file type: ')
#'classinfo.txt'
out_loc = input('Copy location (/): ')
#'/Python Class/Copied Files/'
with open(file_name, 'r') as f:
    read_data = f.read()
    f.closed
#'/Python Class/Copied Files/classinfo_copy.txt'
    out_file = out_loc + "/" + file_name
    with open(out_file, 'w') as f1:
        for line in read_data:
            f1.write(line)


