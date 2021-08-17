# top n most common word in file.
dic = dict()
try:
    fname = input('Enter the file name: ')
    with open(fname, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                dic[word] = dic.get(word, 0) + 1
except:
    print('File name invalid')

tup_as_list = dic.items()
lst = list()
# to ascending sort by value
for k, v in tup_as_list:
    lst.append((k, v))
value_as_sort = sorted(lst)
for topk, topv in value_as_sort[:3]:
    print(topk, topv)

# line comprehension -  create dynamic list
# dict to sorted by value print one line
di = {'a': 10, 'b': 1, 'c': 22}
print(sorted((v, k) for k, v in di.items()))
