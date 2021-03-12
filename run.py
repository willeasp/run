#!/usr/bin/python3

import sys, getopt, os

def help(full=False):
    if full:
        print("FULL HELP")
    else:
        print('run.py [OPTIONS] [ARGUMENTS]')
        print("Type run --help to see instructions.")

def getFileNameType(file):
    fileName, fileType = os.path.splitext(file)
    return fileName, fileType

def addOptions(argv):
    command = ""
    try:
        options, arguments = getopt.getopt(argv[1:], "ti:o:", "help")
    except getopt.GetoptError:
        print("failed to get opts")
        help()
        sys.exit(2)
    for opt, arg in options:
        if opt in ("-t", "--test"):
            command += " -t "
        if opt in ("-i", "--ifile"):
            command += "< " + arg + " "
        if opt in ("-o", "--ofile"):
            command += "> " + arg + " "
    for argument in arguments:
        command += argument + " "
    return command

def compileFile (file):
    fileName, fileType = getFileNameType(file)
    compile_command = "gcc " + file + " -o " + fileName
    return compile_command
        
def main(argv):
    file = argv[0]
    fileName, fileType = getFileNameType(file)
    compile_command = compileFile(file)
    run_command =  "./" + fileName + addOptions(argv)
    full_command = compile_command + " && " + run_command
    os.system(full_command)
    remove_bin = "rm " + fileName
    os.system(remove_bin)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Type the name of the file you want to compile and run.")
        help()
        sys.exit(0)
    if sys.argv[1] in "--help":
        help(full=True)
        sys.exit(0)
    main(sys.argv[1:])