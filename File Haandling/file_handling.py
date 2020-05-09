from colorama import *
# to open a file
# open('location', 'mode') as <filename>: <---this style closes automatically.
# only read mode. (if we do not specify 'r' in place of mode then by default will be 'r'.)

# logic of all mode.
# w : write data into file, it deletes previously present data of the file.
# r : read data from the file, the file pointer  is positioned at start of the file.
# a : to append the data in the file, file pointer is placed at the end of the file,
    # it will create new file when file does not exists, cannot read from file.
# w+ : same function as w but have functions to read from the file.
#  r+ : it is the most dangerrous mode, it read/ writes from the file
    #  it replaces character from file, it does not delete previous data of file.
# a+ : same function as a but it have addition quality to read from file.

# basic functions.
# READ   <----->
# read() <-----> write()
# readline() <----->   nothing
# readlines()<-----> writelines()   for functions check below.


lst = ['hello world\n','i am still\n', 'alive']   # can be used with writelines()

print(Fore.CYAN,'read only mode.\n "with read(): reads whole file at one time.\n "', Fore.RESET)
with open("C:\\Users\\Lenovo\\PycharmProjects\\Practice\\program\\Testfile.txt", "r", 1) as f:
    file = f.read()   # gives whole file    read(5) only read 5 characters from the file.
    print(file)

print(Fore.CYAN,'read only mode.\n "with readlines(): gives all lines in list form.\n "', Fore.RESET)
with open("C:\\Users\\Lenovo\\PycharmProjects\\Practice\\program\\Testfile.txt", "r") as f:
    file = f.readlines()  # gives file in form of list and can be indexed.
    print(file)
    f.seek(0)
    file1 = f.read().splitlines()  # to removes \n from list
    print(file1)

print(Fore.CYAN,'read only mode.\n "with readline():read file line by line.\n "', Fore.RESET)
with open("C:\\Users\\Lenovo\\PycharmProjects\\Practice\\program\\Testfile.txt", "r") as f:
    print(f.readline())  # read line number 1
    print(f.readline())  # read line number 2
    print(f.readline())  # read line number 3

print(Fore.CYAN,' w+(write and read) mode.\n "with write():to write single line in file.\n "', Fore.RESET)
with open("C:\\Users\\Lenovo\\PycharmProjects\\Practice\\program\\Testfile.txt",'w+') as f:
    f.write('hello guys this is new paragraph test.\nthis is new line.\ntere hone se hi mera hona hai.')
    f.seek(0)     # to set the file pointer at arbitotory place.
    print(f.read())

print(Fore.CYAN,' r+(read and write) mode.\n "with write():to write single line in file with replacement of old characters.\n "', Fore.RESET)
with open("C:\\Users\\Lenovo\\PycharmProjects\\Practice\\program\\Testfile.txt", 'r+') as f:
    f.write('world')    # replaces hello w+.
    f.seek(0)
    print(f.read())

# a+ mode.
with open("C:\\Users\\Lenovo\\PycharmProjects\\Practice\\program\\Testfile_new.txt", 'a+') as f:
    f.write('world')    # always add new characters at the end of file.
    f.seek(0)           # no replacement of file is done if seek(0) is done then.
    f.write('hello')    # still it appends at the end.
    f.seek(0)
    print(f.read())
