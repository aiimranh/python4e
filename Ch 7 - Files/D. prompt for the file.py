#  prompt for the file name.
xname = input('Enter the file name with ext:')
xfile = open(xname)
for line in xfile:
    line = line.rstrip()  # avoiding the black line after each line.
    #  this happen due to the every line have \n character and also
    #  the print statement print another new line.
    #  rstrip() remove whiltespace and such type of character that is not print. .
    if not'From:' in line:
        continue
    print(line)

#  prompt for the file name include with bad name:
xname = input('Enter the file name with ext:')
try:
    xfile = open(xname)
except:
    print("Error in file name.")
    quit()
for line in xfile:
    line = line.rstrip()  # avoiding the black line after each line.
    #  this happen due to the every line have \n character and also
    #  the print statement print another new line.
    #  rstrip() remove whiltespace and such type of character that is not print. .
    if not'From:' in line:
        continue
    print(line)
