"""Откройте файл электронной таблицы, содержащей в каждой строке пять натуральных чисел. Определите количество строк таблицы, для которых выполнены оба условия:
– в строке все числа различны;
– удвоенная сумма максимального и минимального чисел строки больше суммы оставшихся трёх её чисел.
В ответе запишите только число"""
# задание_9 -> 1) python задание_9/1.py 2) cd задание_9 python/1.py | cd ..
# set(nums) - переводит список во множество
# with open('1.txt', 'r') as file:
#    for line in file:
#        nums = [int(x.strip()) for x in line.split()]
c = 0
with open('1.txt', 'r') as file:
    for line in file:
        nums = [int(x.strip()) for x in line.split()]
        if len(set(nums)) == len(nums) and 2 * (min(nums) + max(nums)) > sum(nums) - (min(nums) + max(nums)):
            c += 1
print(c)
