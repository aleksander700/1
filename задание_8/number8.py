'''Сколько существует тринадцатеричных семизначных чисел, в которых все цифры различны и никакая нечётная цифра не стоит рядом с цифрой B?'''
from itertools import product
count = 0
for el in product("0123456789ABC", repeat=7):
    number = "".join(el)
    if number[0] == '0':
        continue
    if len(set(number)) < 7:
        continue
    o = {"1", "3", "5", "7", "9", "B"}
    valid = True
    for i in range(7):
        if number[i] == 'B':
            if i > 0 and number[i-1] in o:
                valid = False
                break
            if i < 6 and number[i+1] in o:
                valid = False
                break
    if valid:
        count += 1
print(count)
#5.372.640
