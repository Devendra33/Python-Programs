from os import path

# copying of one file to another file.
if path.isfile('Testfile.txt'):
    with open('Testfile.txt','r') as f1:
        temp = f1.readlines()
        if path.isfile('file_cpy.txt'):
            with open('file_cpy.txt','w+') as f2:
                f2.writelines(temp)
                f2.seek(0)
                print(f2.read())
        else:
            print('file2 does not exists')
            quit()
else:
    print('file1 does not exists')
    quit()