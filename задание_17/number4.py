nums = []
k = 0
m = 0
maxsum = 0
with open('17_27629.txt', 'r') as file:
    for line in file:
        number = int(line.strip())
        nums.append(number)
spis43 = []
for i in range(len(nums)):
    if 1000 <= abs(nums[i]) <= 9999 and abs(nums[i]) % 100 == 43:
        spis43.append(nums[i])
k = max(spis43)
for i in range(len(nums) - 1):
    chetyreha = 1000 <= abs(nums[i]) <= 9999
    chetyrehb = 1000 <= abs(nums[i+1]) <= 9999
    if chetyreha or chetyrehb:
        summ = (nums[i] + nums[i+1]) ** 2
        if summ < k ** 2:
            m += 1
            if summ > maxsum:
                maxsum = summ

print(m, maxsum)
