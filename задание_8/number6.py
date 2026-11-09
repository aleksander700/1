'''Сколько существует чисел, двенадцатеричная запись
которых содержит пять цифр,среди которых есть только две чётные цифры,
причём они равны между собой и стоят рядом.'''
from itertools import *

count = 0
for el in product("0123456789ab", repeat=5):
    number = ''.join(el)
    if number[0] == '0':
        continue

    total_odd = len([x for x in number if x in '02468a'])
    if total_odd != 2:
        continue
    valid = False
    for i in range(4):
        if number[i] in "02468a" and number[i] == number[i+1]:
            valid = True
    if valid:
        count += 1
print(count)
#4968
