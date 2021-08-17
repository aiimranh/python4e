# to create only a file using pass.
with open('mbox-short.txt', 'w') as f:
    pass
    # # to overwrite 'w'
    # # to appendend 'a'
    # f.write("new.txt")

# seek() confusing while writing.
# to write , it does not overwrite full test but the some character
# that you put in to write.
with open('mbox-short.txt', 'w') as f:
    f.write("new\n")
    f.seek(0)
    f.write("D")
