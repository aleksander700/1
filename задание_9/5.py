"""Откройте файл электронной таблицы, содержащий в каждой строке пять натуральных чисел. Определите сумму чисел в строке таблицы с наименьшим номером, содержащей числа, для которых выполнены оба условия:
- в строке все числа различны;
- удвоенная сумма максимального и минимального чисел строки больше суммы оставшихся трёх её чисел.
В ответе запишите только число."""
from collections import Counter
count = 0
with open('5.txt', 'r') as file:
    for line in file:
        nums = [int(x.strip()) for x in line.split()]
        povtor = Counter(nums)
        if len(povtor) == 5 and (2 * (max(nums) + min(nums)) > sum(nums) - max(nums) - min(nums)):
            count += 1
print(count)
