import os
import itertools

# list all files in curdir


def printcurdir():
    '''
    Print all files in active directory
    '''
    print('Files in active directory:\n')
    for f in os.listdir('.'):
        print(f)

def checkfileext(cfile, dfile):
    '''
    Check if copy and destination file have same extension
    '''
    try:
        if dfile.split('.')[1] == cfile.split('.')[1]:
            return True
        else:
            return False
    except ValueError:
        return False

'''
os.mknod("output.txt")

# get current dir path
fname = open('sherlock_small.txt.', 'rb')
outname = open('output.txt', 'wb')

for i in itertools.count():
    record = bytearray(fname.read(16))
    outname.write(record)
    if not record:
        break
'''


if __name__ == '__main__':

    # print current directory
    printcurdir()
    # get file name to copy
    fcheck = True
    while fcheck is True:
        cfile = input('Name of File to copy (filename.ext)\n')
        if os.path.isfile('{}{}{}'.format(os.getcwd(), '/', cfile)):
            print('Found ', cfile)
            fcheck = False
        else:
            print('File not found! Listing available files:\n')
            printcurdir()

    # destination of copied file
    dcheck = True
    while dcheck is True:
        ddir = input('Name of directory for destination file\n')
        if os.path.isdir(ddir):
            print('Found', ddir)
            dcheck = False
        else:
            print(ddir, ' Not Found! Create directory and try again')

    # create destination file
    ccheck = True
    while ccheck is True:
        dfile = input('Name of output file (filename.ext)\n')
        if checkfileext(cfile, dfile) is True:
            ccheck = False
        else:
            print('Problem with {}{} name or extension'.format(cfile, dfile))

    #open copy file
    rcfile = open(cfile, 'rb')
    rdfile = open(os.path.join(ddir, dfile), 'wb')
    for i in itertools.count():
        record = bytearray(rcfile.read(16))
        rdfile.write(record)
        if not record:
            break

    rcfile.close()
    rdfile.close()