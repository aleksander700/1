a = [1, 2, 3, 4, 5, 6]
# 0 -> -1
# 1 -> -2
#
# 2 способ
#
A = []
for i in range(len(a)):
    A.insert(0,a[i])
#a.reverse()
print(*A)
