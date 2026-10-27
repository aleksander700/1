"""В файле содержится последовательность целых чисел. Её элементы могут принимать целые значения от -10 000 до 10 000 включительно. Определите количество троек элементов последовательности, в которых не менее двух трёхзначных чётных чисел, а сумма элементов тройки не меньше минимального положительного четырёхзначного элемента последовательности. В ответе запишите количество найденных троек, затем минимальную из сумм элементов таких троек. В данной задаче под тройкой подразумеваются три идущих подряд элемента последовательности."""
# x => 10<=x<=99 | len(str(number)) == 4
# https://kpolyakov.spb.ru/school/ege/generate.htm
nums = []
minel = 10000
s = 0
minsum = 30000
with open('3.txt', 'r') as file:
    for line in file:
        number = int(line.strip())
        nums.append(number)
        if number < minel and number > 0 and len(str(number)) == 4:
           minel = number
for i in range(1,len(nums) -1):
    a = nums[i-1]
    b = nums[i]
    c = nums[i+1]
    trechznach = 0
    for x in (a,b ,c):
        if 100 <= abs(x) <= 999 and x % 2 == 0:
            trechznach +=1
        
    if (a + b + c) >= minel and trechznach >= 2:
       s +=1
       summ = a + b + c
       if summ < minsum:
           minsum = summ
print(s, minsum)
