from itertools import product
i = 1
"""
for i, el in enumerate(product(sorted("акцент"), repeat=5)):
"""
for el in product(sorted('акцент'), repeat=5):
    word = ''.join(el)
    if i % 2 == 0 and word[0] not in 'аек' and word.count('т') >=1:
        print(i)
        break
    i+=1
