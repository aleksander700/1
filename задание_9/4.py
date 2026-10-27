"""Откройте файл электронной таблицы, содержащей в каждой строке шесть натуральных чисел. Определите наибольший номер строки таблицы, для которой выполнены оба условия:
- в строке все числа различны;
- удвоенная сумма трёх наименьших чисел строки меньше сумма трёх её оставшихся чисел.
ответе запишите только число."""
from collections import Counter
count = 0
with open('3.txt','r') as file:
    for line in file:
        nums = [int(x.strip()) for x in line.split()]
        povtor = Counter(nums)
        nums.sort()
        if len(povtor) == 6 and sum(nums[:3]) < sum(nums[3:]):
            count += 1
print(count)
