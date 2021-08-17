#  searching through the file.
xfile = open('mbox-short.txt')
for line in xfile:
    if line.startswith('From:'):
        print(line)

#  searching through the file.
xfile = open('mbox-short.txt')
for line in xfile:
    line = line.rstrip()  # avoiding the black line after each line.
    #  this happen due to the every line have \n character and also
    #  the print statement print another new line.
    #  rstrip() remove whiltespace and such type of character that is not print. .
    if line.startswith('From:'):
        print(line)

#  another searching through the file using not.
xfile = open('mbox-short.txt')
for line in xfile:
    line = line.rstrip()  # avoiding the black line after each line.
    #  this happen due to the every line have \n character and also
    #  the print statement print another new line.
    #  rstrip() remove whiltespace and such type of character that is not print. .
    if not line.startswith('From:'):
        continue
    print(line)

#  another searching through the file using in.
xfile = open('mbox-short.txt')
for line in xfile:
    line = line.rstrip()  # avoiding the black line after each line.
    #  this happen due to the every line have \n character and also
    #  the print statement print another new line.
    #  rstrip() remove whiltespace and such type of character that is not print. .
    if not 'From:' in line:
        continue
    print(line)
