"""Сколько существует чисел, тринадцатеричная запись которых содержит шесть цифр, 
среди которых есть только три нечётные цифры, причём они равны между собой и стоят рядом."""

# 000001 - 13ичная
# 000001 - 10ичная
from itertools import product
from collections import Counter

count = 0
for el in product("0123456789abc", repeat=6):
    number = ''.join(el)
    
    if number[0] == '0':
        continue
        
    c = Counter(number)
    # c = {
    # "1": 3,
    # "2": 1,
    # "a": 2
    # }
    
    total_odd = sum(count for digit, count in c.items() if digit in "13579b")
    if total_odd != 3:
        continue
        
    valid = False
    for k, val in c.items():
        if k in "13579b" and val == 3:
            if k * 3 in number:
                valid = True
                break
                
    if valid:
        count += 1

print(count)