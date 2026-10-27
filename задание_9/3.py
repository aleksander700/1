"""Откройте файл электронной таблицы, содержащей в каждой строке шесть натуральных чисел. Определите количество строк таблицы, для которых выполнены оба условия:
- в строке есть ровно два числа, каждое из которых повторяется дважды, остальные числа различны;
- сумма всех повторяющихся чисел строки больше суммы всех её неповторяющихся чисел.
В ответе запишите только число."""
from collections import Counter
count = 0
with open('3.txt','r') as file:
    for line in file:
        nums = [int(x.strip()) for x in line.split()]
        povtor = Counter(nums)
        p = [] # список повторов
        np = [] # список неповторов
        c = 0 # счетчик повторяющихся 2 раза эл.
        for el, el_count in povtor.items():
            if el_count == 2:
                c += 1
                p.append(el)
            else:
                np.append(el)
        if c == 2 and len(povtor) == 4 and sum(p)*2 > sum(np):
            count += 1
print(count)
