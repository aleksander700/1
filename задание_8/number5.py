'''Сколько существует чисел, четырнадцатеричная запись которых содержит пять цифр, среди которых есть только две нечётные цифры,
причём они равны между собой и между ними стоит только одна цифра.
'''
from itertools import *
from collections import Counter
count = 0
for el in product("0123456789abcd", repeat=5):
    number = ''.join(el)
    if number[0] == '0':
        continue
    c = Counter(number)
    total_odd = sum(count for digit, count in c.items() if digit in "13579bd")
    if total_odd != 2:
        continue
    valid = False
    for i in range(3):
        if number[i] in "13579bd" and c[number[i]] == 2:
            if number[i] == number[i+2]:
                valid = True
            else:
                break
    if valid:
        count += 1
print(count)
