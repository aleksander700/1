from collections import Counter
c = 0
with open('29962.txt', 'r') as file:
    for count, line in enumerate(file, start=1):
        nums = [int(x.strip()) for x in line.split()]
        povtor = Counter(nums)
        p = []
        n=[]
        for el, el_count in povtor.items():
            if el_count == 3:
                p.append(el)
            if el_count == 1:
                n.append(el)
        if len(p) == 1 and len(n) == 4:
            if sum(n) / 4 > p[0]:
                c = count
print(c)
