"""Сколько существует десятичных четырёхзначных чисел, 
в которых все цифры различны и никакие две чётные или две нечётные цифры не стоят рядом?"""
from itertools import *
count = 0
for el in permutations("0123456789", 4):
    number = ''.join(el)
    if number[0] == '0':
        continue

    l = [int(x) % 2 for x in number]
    
    if l[0] != l[1] and l[1] != l[2] and l[2] != l[3]:
        count += 1
print(count)