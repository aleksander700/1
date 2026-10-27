nums = []
k = 0
maxsum = -300001
minel = -100001
with open('17_28938.txt', 'r') as file:
    for line in file:
        number = int(line.strip())
        nums.append(number)
        if abs(number) % 100 == 28 and number > minel:
            minel = number
for i in range(1,len(nums) -1):
    a = nums[i-1]
    b = nums[i]
    c = nums[i+1]
    d = []
    for x in (a,b ,c):
        if 100 <= abs(x) <= 999:
            d.append(x)
    if len(d) >=1 and 0 < (a + b + c) / 3 < minel:
        k += 1
        if maxsum < a + b + c:
            maxsum = a + b + c
print(k, maxsum)
