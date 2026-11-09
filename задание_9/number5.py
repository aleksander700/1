from collections import Counter
count = 0
with open('27764.txt', 'r') as file:
    for line in file:
        nums = [int(x.strip()) for x in line.split()]
        povtor = Counter(nums)
        if len(povtor) == 5 and (2 * (max(nums) + min(nums)) == sum(nums) - max(nums) - min(nums)):
            count += 1
print(count)
