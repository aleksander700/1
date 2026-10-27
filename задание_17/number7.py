nums = []
k = 0
maxsum = -300001
minel = -100001
with open('17_31225.txt', 'r') as file:
    for line in file:
        number = int(line.strip())
        nums.append(number)
        if 1000 <= abs(number) <= 9999 and abs(number) % 10 == 9:
            if number > minel:
                minel = number
for i in range(1,len(nums) -1):
    a = nums[i-1]
    b = nums[i]
    c = nums[i+1]
    l = []
    for x in [a, b, c]:
        if 1000 <= abs(x) <= 9999 and abs(x) % 10 == 9:
            l.append(x)
    if len(l) == 2:
        summ = a + b + c
        if summ < minel:
            k += 1
            if summ > maxsum:
                maxsum = summ
print(k, maxsum)
