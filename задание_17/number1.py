nums = []
k = 0
maxsum = -200001
minel = 100001
with open('17_29349.txt', 'r') as file:
    for line in file:
        number = int(line.strip())
        nums.append(number)
        if minel > number and number > 0 and number % 123 == 0:
            minel = number
for i in range(len(nums)-1):
    a = nums[i]
    b = nums[i+1]
    if a + b < minel:
        k += 1
        if maxsum < a + b:
            maxsum = a+b
print(k, maxsum)
