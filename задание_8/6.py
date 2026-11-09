"""Определите, сколько пятизначных чисел,
записанных в семеричной системе счисления, содержат ровно одну цифру 0 и не более двух цифр 1"""
from itertools import *
from collections import Counter
count = 0
for el in product('0123456', repeat=5):
    number = ''.join(el)
    if number[0] == '0':
        continue
    if number.count('0') == 1 and number.count('1') <= 2:
        count += 1
print(count)
