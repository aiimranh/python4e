# contact manager auto close() the file.
# outside of the loop file will be closed.
# read() fn
with open('mbox-short.txt', 'r') as f:
    f_content = f.read()
    # read() fn make total file into a string.
    # read(size), here size is the return bytes.
    print(f_content)

# readline() fn
with open('mbox-short.txt', 'r') as f:
    f_content = f.readline()
    # readline() fn read the first line of the file.
    print(f_content, end='')
    # end='' to prevent extra newline, that use print fn.
    f_content = f.readline()
    # readline() fn read the 2nd line of the file.
    print(f_content, end='')
    # readline() fn read the next line of the file.

# readline() fn
with open('mbox-short.txt', 'r') as f:
    f_content = f.readline(10)
    # readline() fn read the first line of the file.
    # readline(size) , size is the return bytes of the selected line.
    # readline() call again means print next line.
    print(f_content, end='')
    # end='' to prevent extra newline, that use print fn.

# readlines() fn
with open('mbox-short.txt', 'r') as f:
    f_content = f.readlines()
    # readlines() fn Return all lines in the file,
    # as a list where each line is an item in the list object.
    # readlines(hint) fn hint is Optional. If the number of bytes returned exceed the hint number,
    # no more lines will be returned. Default value is  -1,
    # which means all lines will be returned..
    print(f_content)
