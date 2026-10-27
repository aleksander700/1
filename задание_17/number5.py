nums = []
k = 0
minsum = 200001
minel = -100001
with open('17_27301.txt', 'r') as file:
    for line in file:
        number = int(line.strip())
        nums.append(number)
        if str(abs(number)).startswith('45'):
            if number > minel:
                minel = number
for i in range(1,len(nums) -1):
    a = nums[i-1]
    b = nums[i]
    c = nums[i+1]
    l = []
    for x in [a, b, c]:
        if x < 0:
            l.append(x)
    if len(l) == 1:
        summ = a + b + c
        if summ >= minel:
            k += 1
            if abs(summ) % 100 == 45:
                if summ < minsum:
                    minsum = summ
print(k, minsum)
