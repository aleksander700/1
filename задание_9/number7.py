count = 0
with open("27287.txt", "r") as f:
    for line in f:
        count += 1
        nums = [int(x) for x in line.split()]
        p = [x for x in nums if nums.count(x) == 3]
        n = [x for x in nums if nums.count(x) == 1]
        c1 = len(p) == 6 and len(set(p)) == 2 and len(n) == 1
        if c1:
            c2 = n[0] <= min(p)
            if c2:
                print(abs(max(p)))
                break
