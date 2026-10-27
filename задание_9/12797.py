c = 0
with open('12797.txt', 'r') as file:
    for line in file:
        nums = [int(x.strip()) for x in line.split()]
        if len(set(nums)) == 3 and all(x % 2 == 0 for x in set(nums) if nums.count(x) == 2) and all(x % 2 != 0 for x in set(nums) if nums.count(x) == 1):
            c += 1
print(c)
