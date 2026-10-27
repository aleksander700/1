import itertools
a = 'ELNOSC'
words = itertools.product(a, repeat=6)
i = 1
lastnumber = 0
lastword = ''
for el in words:
    word = ''.join(el)
    if i %2 != 0 and word[0] not in 'CN' and word.count('C') == 1 and word.count('N') ==1:
        lastnumber = i
        lastword = word
    i += 1
print(lastnumber)
print(lastword)

'''import itertools

a = 'ELNOSC'
words = reversed(list(itertools.product(a, repeat=6)))
combinations = 6**6
for index, el in enumerate(words):
    word = ''.join(el)
    i = combinations - index
    if i % 2 != 0 and word[0] not in 'CN' and word.count('C') == 1 and word.count('N') == 1:
        print(i)
        print(word)
        break'''
