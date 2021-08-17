# dict() count
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        # in / not in operator mostly use in dictionary.
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

# dict() count with get() method
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
counts = dict()
for name in names:
    counts[name] = counts.get(name, 0) + 1
    # counts.get(name, 0) means if name not have
    # there by default it will bw zero.
print(counts)

# counting words in text from file
counts = dict()
with open('mboxx.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        words = line.split()
        # here words in a list()
        for word in words:
            counts[word] = counts.get(word, 0) + 1
big_count = None
big_word = None
for word, count in counts.items():
    if big_count is None or count > big_count:
        big_count = count
        big_word = word
print(big_word, big_count)
