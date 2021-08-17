# to print separator after a specific bytes or character.

with open('mbox-short.txt', 'r') as f:
    size = 30
    f_content = f.read(size)
    # read() fn make total file into a string.
    # read(size), here size is the return bytes.
    print(f.tell())
    # file.tell() fn return where you are.
    f.seek(0)
    # file.seek(offset) fn return to the specific point
    # where offset indicate the specified position.
    while len(f_content) > 0:
        print(f_content, end='***')
        f_content = f.read(size)
