# reading and making a copy of text.
# generally it use utf-8 codec.
with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)  # copy line by line.

# reading and making a copy of picture.
# we have to use binary mode.
with open('pen.jpg', 'rb') as rf:
    with open('pen_copy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)  # copy line by line.

# reading and making a copy of text.
# generally it use utf-8 codec.
with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        specific = 2048
        rf_spec = rf.read(specific)  # read first 2048 bytes
        while len(rf_spec) > 0:  # until the all bytes copy
            wf.write(rf_spec)  # copy that 2048 bytes.
            rf_spec = rf.read(specific)  # read next 2048 bytes
