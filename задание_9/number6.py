
count = 0
with open('27621.txt', 'r') as file:
    for line in file:
        count += 1
        nums = [int(x.strip()) for x in line.split()]
        if len(set(nums)) == 5 and (max(nums) - min(nums)) == (sum(nums) - max(nums) - min(nums)):
            print(count)
            break
