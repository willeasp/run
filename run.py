#!/usr/bin/python3

import sys, getopt, os.path, subprocess

def help(full=False):
    if full:
        pass
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
        if opt in "--help":
            help(full=True)
            sys.exit()
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
    print("Compiling: " + compile_command)
    subprocess.run(compile_command.split())
        
def main(argv):
    file = argv[0]
    fileName, fileType = getFileNameType(file)
    compileFile(file)
    run_command =  "./" + fileName + addOptions(argv)
    print("Running: " + run_command)
    subprocess.run(run_command.split())

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Type the name of the file you want to compile and run.")
        help()
        sys.exit(0)
    main(sys.argv[1:])