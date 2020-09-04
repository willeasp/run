#!/usr/bin/python3

import sys, getopt, os

# ,"hi:o:",["ifile=","ofile="]

def help(full=False):
    if full:
        pass
    else:
        print('run.py [OPTIONS] [ARGUMENTS]')
        print("Type run --help to see instructions.")

def getFileNameType(file):
    fileName, fileType = os.path.splitext(file)
    return fileName, fileType

def main(argv):
    if len(argv) == 0:
        print("Type the name of the file you want to compile and run.")
        help()
    command = ""
    print(argv[1:])
    try:
        options, arguments = getopt.getopt(argv[1:], "ti:o:", "help")
    except getopt.GetoptError:
        print("failed to get opts")
        help()
        sys.exit(2)

    """ for opt, arg in opts:
        if opt == '--help':
            print(help)
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-t", "--test"):
            arguments.append(opt)
    print("Arguments is: ", )
    print('Input file is: ', inputfile)
    print('Output file is: ', outputfile) """

if __name__ == "__main__":
   main(sys.argv[1:])