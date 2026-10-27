import itertools
a = 'ABC'
k = 3
c = 0
words = itertools.product(a, repeat=k)
for el in words:
    word =  ''.join(el)
    print(word)

    if word.count(a[0]) > 1:
        c += 1
print(c)
