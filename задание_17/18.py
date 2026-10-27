nums = []
minel = 100001
with open('17_31514.txt', 'r') as file:
    for line in file:
        number = int(line.strip())
        nums.append(number)
        if minel > number:
            minel = number
# minel = min(nums) 
c = 0
maxsum = 0
for i in range(len(nums)-1): # len(nums) = 10000; последний индекс - 9999; 
    a = nums[i]
    b = nums[i + 1] # !!! 10000 -> 9999 -> i + 1 = 10000
    if a % 33== minel or b % 33 == minel:
        c += 1
        summ = a + b
        if summ > maxsum:
            maxsum = summ
print(c, maxsum)
