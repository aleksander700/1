
count = 0
with open('29341.txt', 'r') as file:
    for line in file:
        nums = sorted(map(int, line.split()))
        c1 = nums[3] < (nums[0] + nums[1] + nums[2])
        c2 = ((nums[0] + nums[3] != nums[1] + nums[2]) and (nums[0] + nums[1] != nums[2] + nums[3]) and (nums[0] + nums[2] != nums[1] + nums[3]))
        count += c1 and c2
print(count)
