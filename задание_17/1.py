"""В файле содержится последовательность целых чисел.
Её элементы могут принимать целые значения от -100 000 до 100 000 включительно.
Определите количество троек элементов последовательности, в которых ровно два двузначных числа,
а квадрат суммы элементов тройки меньше максимального элемента последовательности, оканчивающегося на 33.
В ответе запишите количество найденных троек чисел, затем максимальную из сумм элементов таких троек.
данной задаче под тройкой подразумевается три идущих подряд элемента последовательности."""
maxel = 0
maxsum = 0
s = 0
nums = []
with open('1.txt', 'r') as file:
    for line in file:
        number = int(line.strip())
        nums.append(number)
        if number > maxel and number % 100 == 33:
           maxel = number
for i in range(1, len(nums)-1):
    a = nums[i-1]
    b = nums[i]
    c = nums[i+1]
    dvuznach = 0
    for x in (a, b ,c):
        if 10 <= abs(x) <= 99:
            dvuznach += 1
    if dvuznach == 2:
        summ = a+b+c
        if summ **2 < maxel:
            s += 1
            if summ > maxsum:
                maxsum = summ
print(s, maxsum)
