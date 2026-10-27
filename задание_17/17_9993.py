"""В файле содержится последовательность целых чисел, по модулю не превышающих 100 000. 
Определите количество пар элементов последовательности, в которых только одно число является простым, 
а сумма элементов пары кратна максимальному элементу последовательности, оканчивающемуся на 17. 
В ответе запишите два числа: сначала количество найденных пар, затем максимальное произведение элементов пары. 
В данной задаче под парой подразумевается два идущих подряд элемента последовательности. 17_9993.txt"""
def simple(n):
    for d in range(2, int(abs(n**0.5))+1):
        if n % d == 0:
            return 0
    return 1

nums = []
maxel = -100001
count = 0
maxpr = -10000000000
with open('17_9993.txt', "r") as file:
    for line in file:
        number = int(line.strip())
        nums.append(number)
        if number > maxel and abs(number) % 100 == 17:
            maxel = number
for i in range(len(nums)-1):
    a = nums[i]
    b = nums[i+1]
    if simple(a)+simple(b) == 1 and (a+b) % maxel == 0:
        count+=1
        if a*b > maxpr:
            maxpr = a*b 

print(count, maxpr)
#int() argument must be a string, a bytes-like object or a real number, not 'complex'
# 6 2446423792