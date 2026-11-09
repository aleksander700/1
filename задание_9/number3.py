
count = 0
with open('28930.txt', 'r') as file:
    for line in file:
        nums = [int(x.strip()) for x in line.split()]
        c1 = nums[0] < nums[1] < nums[2] < nums[3] < nums[4]
        minmax = min(nums) + max(nums)
        r = sum(nums) - minmax
        c2 = minmax <= r
        count += c1 and c2
print(count)
