N = int(input())
a = []
for i in range(N):
    b = int(input())
    a.append(b)
# c = [int(input()) for j in range(N)]
x = int(input())
c = 0 # schetchik
for el in a:
    if el == x:
        c += 1
print(*a)
print(c)



print(a.count(x)) # короткое решение