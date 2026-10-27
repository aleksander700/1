nums = []
k = 0
maxsum = -300001
minel = 100001
with open('17_28762.txt', 'r') as file:
    for line in file:
        number = int(line.strip())
        nums.append(number)
        if number % 23 == 0 and number < minel:
            minel = number
for i in range(len(nums) - 1):
    a = nums[i]
    b = nums[i+1]
    if a % minel == 0 or b % minel == 0:
        k += 1
        if maxsum < a + b:
            maxsum = a + b
print(k, maxsum)
