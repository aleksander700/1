"""Откройте файл электронной таблицы, содержащей в каждой строке шесть натуральных чисел. Определите количество строк таблицы, состоящих из чисел, для которых выполнены оба условия:
- в строке только одно число повторяется трижды, остальные числа различны;
- куб повторяющегося числа строки меньше произведения всех её неповторяющихся чисел.
В ответе запишите только число."""
from collections import Counter
count = 0
with open('2.txt', 'r') as file:
    for line in file:
        nums = [int(x.strip()) for x in line.split()]
        povtor = Counter(nums) # dict {число: повтор}
        el_povtor = 0
        for el, el_count in povtor.items(): # пробегаемся по всем значениям
            if el_count == 3:
                el_povtor = el

        if el_povtor != 0 and len(povtor) == 4 and el_povtor**3 < :
        # povtor = 0
        # nums_1 = set(nums)
        # for i in range(4):
        #     if nums.count(nums[i]) == 3:
        #         povtor = nums[i]
        # if povtor != 0: nums_1.remove(povtor)
        # nums_1 = list(nums)
        # if ( nums.count(nums[0]) == 3 or nums.count(nums[1]) == 3 or nums.count(nums[2]) == 3 or nums.count(nums[3])  ) and len(set(nums)) == 4 and  povtor**3 < nums_1[0]*nums_1[1]*nums_1[2]:
        #     count +=1
print(count)
